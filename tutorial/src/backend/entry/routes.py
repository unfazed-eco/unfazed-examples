from unfazed.route import include, path

patterns = [
    path("/enroll", routes=include("enroll.routes")),
]
