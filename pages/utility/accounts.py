class Accounts:

    # These would all be stored in a secure secret manager IRL, and would never be checked into source control.
    # Since they are displayed publicly on the demo site, I didn't worry about security here.
    STANDARD_USER = 'standard_user'
    LOCKED_OUT_USER = 'locked_out_user'
    PROBLEM_USER = 'problem_user'
    PERFORMANCE_GLITCH_USER = 'performance_glitch_user'
    ERROR_USER = 'error_user'
    VISUAL_USER = 'visual_user'

    DEFAULT_PASSWORD = 'secret_sauce'
