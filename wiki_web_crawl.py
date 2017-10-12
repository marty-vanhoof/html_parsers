
def continue_crawl(search_history, target_url):
    '''decide whether to continue to crawl each webpage based on conditions.
    Returns False to stop crawling, otherwise the function returns True.'''

    if search_history[-1] == target_url:
        print("Target article found!")
        return False
    elif len(search_history) > 25:
        print("The search is going on too long; aborting search!")
        return False
    elif len(search_history) != len(set(search_history)):
        print("We are back to an article we've already seen; aborting search!")
        return False
    else:
        return True