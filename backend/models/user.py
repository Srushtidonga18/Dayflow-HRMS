from database.db_connection import get_db_connection

class UserModel:

    @staticmethod
    def create_user(employee_id, company_code, first_name, last_name,
                    email, phone, password_hash, role, year_of_joining):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO hrms.users
            (employee_id, company_code, first_name, last_name, email, phone,
             password_hash, role, year_of_joining)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            RETURNING id
        """, (
            employee_id, company_code, first_name, last_name,
            email, phone, password_hash, role, year_of_joining
        ))

        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return user_id

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM hrms.users WHERE email=%s", (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user
