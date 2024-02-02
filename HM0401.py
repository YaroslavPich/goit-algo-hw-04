from pathlib import Path


def total_salary(path: str) -> tuple:
    """Finding the amount of wages and average wages"""
    total_average = [0, 0]
    employee_dict = {}
    path = Path(path)
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines() if el.strip()]
    except Exception as e:
        print(
            f"Помилка читання файлу: {e}.\n\
Перевірте наявність файл та перезапустіть програму!"
        )
        exit()

    if len(lines) == 0:
        print(
            "В файлі немає інформації.\n\
Перевірте чи в файлі є записи з потрібною інформацією"
        )
        exit()

    for el in lines:
        name, salary_str = el.split(",")
        salary = float(salary_str)
        employee_dict[name] = salary
    total = round(sum(employee_dict.values()), 2)
    number_employees = len(employee_dict.keys())
    try:
        average = round(total / number_employees, 2)
    except ZeroDivisionError:
        print("Немає працівників!")
    total_average[0] = total
    total_average[1] = average
    total_and_average = tuple(total_average)
    return total_and_average


total, average = total_salary("salary_file.txt")
print(
    f"Загальна сума заробітної плати: {total:.2f}\n\
Середня заробітна плата: {average:.2f}"
)
