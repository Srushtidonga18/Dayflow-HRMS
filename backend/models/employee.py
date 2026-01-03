from database.db_connection import get_db_connection

class EmployeeProfileModel:

    @staticmethod
    def create_profile(user_id, first_name, last_name, phone,
                       dob, gender, designation, department, doj):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO hrms.employee_profiles
            (user_id, first_name, last_name, phone, date_of_birth,
             gender, designation, department, date_of_joining)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            user_id, first_name, last_name, phone,
            dob, gender, designation, department, doj
        ))

        conn.commit()
        cur.close()
        conn.close()
