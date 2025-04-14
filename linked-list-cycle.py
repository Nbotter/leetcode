def create_node(val):
    return {'val': val, 'next': None}

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.get('next'):
        slow = slow['next']
        fast = fast['next']['next']

        if slow == fast:
            return True

    return False