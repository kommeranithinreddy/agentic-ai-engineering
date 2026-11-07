#The dependent function's behavior is influenced by the dependency.

def get_ticket_priority(ticket_id): #Dependency function
    #Business Logic
    return "High"


def process_ticket(ticket_id, reference_function): #Dependency function is passing through Dependency injection
    priority = reference_function(ticket_id)
    return priority


def mock_get_ticket_priority(ticket_id): #Test mock dependency function
    return "Low"


assert process_ticket(101, get_ticket_priority) == "High"
assert process_ticket(101, mock_get_ticket_priority) == "Low"