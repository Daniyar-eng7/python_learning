-- 1. Upsert — добавить или обновить если уже существует
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        -- контакт есть — обновляем телефон
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
        RAISE NOTICE 'Обновлён: %', p_name;
    ELSE
        -- контакта нет — добавляем
        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
        RAISE NOTICE 'Добавлен: %', p_name;
    END IF;
END;
$$;


-- 2. Массовая вставка с проверкой номера
CREATE OR REPLACE PROCEDURE bulk_insert(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_data TEXT := '';  -- сюда копим неправильные данные
BEGIN
    FOR i IN 1..array_length(p_names, 1) LOOP
        -- проверяем: номер должен начинаться с + и содержать только цифры
        IF p_phones[i] ~ '^\+[0-9]+$' THEN
            -- номер правильный — вставляем
            CALL upsert_contact(p_names[i], p_phones[i]);
        ELSE
            -- номер неправильный — добавляем в список ошибок
            invalid_data := invalid_data || p_names[i] || ':' || p_phones[i] || '; ';
        END IF;
    END LOOP;

    IF invalid_data <> '' THEN
        RAISE NOTICE 'Неправильные данные: %', invalid_data;
    END IF;
END;
$$;


-- 3. Удаление по имени или телефону
CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR DEFAULT NULL,
                                           p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
        RAISE NOTICE 'Удалён по имени: %', p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
        RAISE NOTICE 'Удалён по телефону: %', p_phone;
    ELSE
        RAISE NOTICE 'Укажи имя или телефон!';
    END IF;
END;
$$;



