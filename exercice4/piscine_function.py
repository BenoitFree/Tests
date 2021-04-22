from evaluation.exercice4.PiscineLogic import PiscineLogic


def start_heating(piscine_logic: PiscineLogic):
    last_days_temps = piscine_logic.get_last_days_temps()
    temperature_moyenne_derniers_jours = sum(last_days_temps)/len(last_days_temps)

    if(temperature_moyenne_derniers_jours > 20) and piscine_logic.get_actual_temp() > 25:
        piscine_logic.set_heater(True)
        return True
    else:
        piscine_logic.set_heater(False)
        return False
