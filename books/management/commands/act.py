from django.core.management import BaseCommand, CommandError


#
# class Command(BaseCommand):
#     """ simple """
#     def add_arguments(self, parser):
#         parser.add_argument('positional')
#         parser.add_argument('--opt') # when make dict \+ options['opt'] БЕЗ --opt (or -opt)
#
#     def handle(self, *args, **options):
#         print(f'First one: {options["positional"]}')
#         print(f'Optional: {options["opt"]}')
#         # options: {'verbosity': 1, 'settings': None, 'pythonpath': None,
#         # 'traceback': False, 'no_color': False, 'force_color': False, 'skip_checks': False}
#
#         return "zziii"

class Command(BaseCommand):
    """more features """

    def add_arguments(self, parser):
        parser.add_argument('pos', type=int, help="Should be int less or equal 34")
        parser.add_argument('-opt', default="snow", help="this is not required")

    def handle(self, *args, **options):
        if options["pos"] <= 34:
            self.stdout.write(self.style.SUCCESS('Yes!!!!!!!!!!'))

        else:
            raise CommandError("arg should be less or = 34 S")
        self.stdout.write(f'found in cmd optional param: {options["opt"]}')
