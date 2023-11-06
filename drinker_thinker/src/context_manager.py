from drinker_thinker.src.io.query_runner import QueryRunner


class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()

    def record_drinks(self, num_drinks, comment, date):
        self.query_runner.record_drinks(num_drinks, comment, date)

    def get_drinks(self):
        return self.query_runner.read_drinks()
