from unittest.mock import Mock

mock_function = Mock()
mock_function.return_value = "Low"



def process_ticket(ticket_id, reference_function):
    priority = reference_function(ticket_id)
    return priority


assert process_ticket(101, mock_function) == "Low"
mock_function.assert_called_once_with(101) #checks what mock function receives as parameter