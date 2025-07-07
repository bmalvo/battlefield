"""Function should return a dictionary/Object/Hash with "status" as a key, 
whose value can : "busy" or "available" depending on the truth value of the 
argument is_busy.

But as you will see after clicking RUN or ATTEMPT this code has several bugs, 
please fix them."""


def get_status(is_busy):
    """Returns a dictionary with the status based on the input."""
    status = "busy" if is_busy else "available"
    return {'status': status}
