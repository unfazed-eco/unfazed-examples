from unfazed.route import include, path

# from yourapp.routes import patterns

"""

example:

patterns = [
    path("/index", endpoint="index"),
    path("/api/account", routes=include("account.routes")),
    path("/api/auth", routes=patterns),
]


"""

patterns = [
    path("/api/enroll", routes=include("enroll.routes")),
]
