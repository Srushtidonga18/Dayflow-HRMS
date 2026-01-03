from database.db_connection import get_db_connection

class LeaveModel:

    @staticmethod
    def apply_leave(user_id, leave_type_id, start_date, end_date, reason):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO hrms.leave_requests
            (user_id, leave_type_id, start_date, end_date, reason)
            VALUES (%s,%s,%s,%s,%s)
        """, (
            user_id, leave_type_id, start_date, end_date, reason
        ))

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_user_leaves(user_id):
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT lr.id, lt.name, lr.start_date, lr.end_date, lr.status
            FROM hrms.leave_requests lr
            JOIN hrms.leave_types lt ON lr.leave_type_id = lt.id
            WHERE lr.user_id=%s
        """, (user_id,))

        leaves = cur.fetchall()
        cur.close()
        conn.close()
        return leaves
