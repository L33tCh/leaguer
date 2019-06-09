import leaguer as app
from unittest import mock
from unittest.mock import patch
import io


class TestMain:
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input(self, mock_stdout):
        inputs = [
            "Lions 3, Snakes 3",
            "Tarantulas 1, FC Awesome 0",
            "Lions 1, FC Awesome 1",
            "Tarantulas 3, Snakes 1",
            "Lions 4, Grouches 0",
            ""
        ]

        with mock.patch('builtins.input', side_effect=inputs):
            app.main()
            assert mock_stdout.getvalue().strip() == "\n".join([
                "1. Tarantulas, 6 pts",
                "2. Lions, 5 pts",
                "3. FC Awesome, 1 pt",
                "3. Snakes, 1 pt",
                "5. Grouches, 0 pts"
            ])
