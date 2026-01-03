from database.db_connection import get_db_connection

class AttendanceModel:

    @staticmethod
    def mark_attendance(user_id, date, check_in, check_out, status, work_hours):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO hrms.attendance
            (user_id, date, check_in, check_out, status, work_hours)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            user_id, date, check_in, check_out, status, work_hours
        ))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_user_attendance(user_id):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT date, check_in, check_out, status, work_hours
            FROM hrms.attendance
            WHERE user_id=%s
            ORDER BY date DESC
        """, (user_id,))

        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
