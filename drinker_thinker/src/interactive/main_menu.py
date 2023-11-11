from datetime import datetime

from interactive_menu.src.interactive_menu import InteractiveMenu


class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            RecordMenu(manager, self.path),
            TotalsMenu(manager, self.path),
            GraphsMenu(manager, self.path)
        ]

    def title(self):
        return "Main"

class RecordMenu(InteractiveMenu):

    def title(self):
        return "Record"

    def main_loop(self):
        form_results = self.interactive_form(
            [
                {
                    "question": "How many drinks did you have?",
                    "expected_response_type": "INT",
                    "return_as": "num_drinks",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "Comment? (Hit enter for no comment)",
                    "expected_response_type": "VARCHAR",
                    "return_as": "comment",
                    "default": "",
                    "allow_empty": True
                },
                {
                    "question": "What date? (YYYY-MM-DD) Hit enter for today",
                    "expected_response_type": "YYYYMMDD_Date",
                    "return_as": "date",
                    "default": datetime.now().strftime("%Y-%m-%d"),
                    "allow_empty": False
                }
            ]
        )
        if form_results["user_accept"] != True:
            print("Aborting!")
            return
        form_results.pop("user_accept")
        for answer_key in form_results.keys():
            if not form_results[answer_key]["valid"]:
                print("%s is not a valid value! Aborting" % answer_key)
                return

        num_drinks = form_results["num_drinks"]["value"]
        comment = form_results["comment"]["value"]
        date = form_results["date"]["value"]

        print("%s drinks on %s -- %s" % (num_drinks, date, comment))
        self.manager.record_drinks(num_drinks, comment, date)

class TotalsMenu(InteractiveMenu):

    def title(self):
        return "Totals"

    def main_loop(self):
        results = self.manager.get_drinks()
        for result in results:
            print(result)

class GraphsMenu(InteractiveMenu):

    def title(self):
        return "Graphs"

    def main_loop(self):
        self.manager.heat_graph()
