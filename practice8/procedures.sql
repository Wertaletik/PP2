ALTER TABLE contacts
ADD CONSTRAINT unique_name UNIQUE(name);



CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO contacts(name, phone)
    VALUES (p_name, p_phone)
    ON CONFLICT (name)
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$;



CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    invalid_data := ARRAY[]::TEXT[];

    IF array_length(names, 1) IS DISTINCT FROM array_length(phones, 1) THEN
        RAISE EXCEPTION 'Arrays must have same length';
    END IF;

    FOR i IN 1..COALESCE(array_length(names, 1), 0) LOOP
        
        IF phones[i] ~ '^[0-9]{5,15}$' THEN
            
            INSERT INTO contacts(name, phone)
            VALUES (names[i], phones[i])
            ON CONFLICT (name)
            DO UPDATE SET phone = EXCLUDED.phone;

        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;

    END LOOP;
END;
$$;



CREATE OR REPLACE PROCEDURE delete_contact_proc(value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = value OR phone = value;
END;
$$;