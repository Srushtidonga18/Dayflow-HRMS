from database.db_connection import get_db_connection

class PayrollModel:

    @staticmethod
    def add_payroll(user_id, basic, allowances, deductions, net, month):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO hrms.payroll
            (user_id, basic_salary, allowances, deductions, net_salary, month)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            user_id, basic, allowances, deductions, net, month
        ))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_user_payroll(user_id):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT month, net_salary, created_at
            FROM hrms.payroll
            WHERE user_id=%s
        """, (user_id,))

        payroll = cur.fetchall()
        cur.close()
        conn.close()
        return payroll
