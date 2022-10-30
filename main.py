import application.salary as number
from application.db.people import get_employees as employee
from datetime import datetime
from application.youtube import get_video_info as video_info


if __name__ == '__main__':
    number.calculate_salary()
    employee()
    date_now = datetime.today()
    print(f'Текущая дата: {date_now.date()}')
    video_info()
