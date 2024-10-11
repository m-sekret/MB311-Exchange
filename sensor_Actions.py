# Змінні для зберігання значень сенсорів
ABM = None  # Значення сенсора ABM
BTI = None  # Значення сенсора BTI
KO = None   # Значення сенсора KO

def update_sensors(abm_value, bti_value, ko_value):

    #Функція для оновлення значень сенсорів.
    
    global ABM, BTI, KO
    ABM = abm_value
    BTI = bti_value
    KO = ko_value
    print(f"Сенсори оновлено: ABM={ABM}, BTI={BTI}, KO={KO}")

def get_sensor_values():
    """
    Функція для отримання значень сенсорів.
    """
    return {
        "ABM": ABM,
        "BTI": BTI,
        "KO": KO
    }

if __name__ == "__main__":
    # Приклад використання
    update_sensors(10, 20, 30)
    values = get_sensor_values()
    print(values)
