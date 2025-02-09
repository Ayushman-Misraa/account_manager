from PyQt5.QtWidgets import QLabel

class SummaryManager:
    @staticmethod
    def update_summary(transactions, summary_labels):
        total_credit = total_debit = net_balance = money_given = money_taken = 0.0

        for trans in transactions:
            amount = trans['amount']
            if trans['type'] == 'Credit':
                total_credit += amount
            else:
                total_debit += amount

            if trans['status'] == 'Given':
                money_given += amount
            elif trans['status'] == 'Taken':
                money_taken += amount

        net_balance = total_credit - total_debit

        summary_labels['credit'].setText(f"Total Credit:\n₹{total_credit:,.2f}")
        summary_labels['debit'].setText(f"Total Debit:\n₹{total_debit:,.2f}")
        summary_labels['balance'].setText(f"Net Balance:\n₹{net_balance:,.2f}")
        summary_labels['given'].setText(f"Money Given:\n₹{money_given:,.2f}")
        summary_labels['taken'].setText(f"Money Taken:\n₹{money_taken:,.2f}")