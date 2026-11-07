from unittest.mock import Mock

mock_function = Mock()
mock_function.side_effect = RuntimeError("API unavailable")


def process_ticket(ticket_id, reference_function):
    priority = reference_function(ticket_id)
    return priority



try:
    process_ticket(101, mock_function)
except RuntimeError as e:
    print(e)

mock_function.assert_called_once_with(101)