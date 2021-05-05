import schema

schemas = {
    "/api/admin/login":
        schema.Schema({
            "username": str,
            "passwd": str
        }),
    "/api/admin/passwd":
        schema.Schema({
            "username": str,
            "oldPasswd": str,
            "newPasswd": str
        }),
    "/api/admin/userlist":
        schema.Schema({}),
    "/api/admin/createUser":
        schema.Schema({
            "username": str,
            "passwd": str
        }),
    "/api/admin/removeUser":
        schema.Schema({
            "username": str,
            "passwd": str
        }),
    "/api/admin/DBInfo":
        schema.Schema({}),
    "/api/admin/setTimeout":
        schema.Schema({
            "interactiveTimeout": int,
            "waitTimeout": int
        }),
    "/api/admin/setCache":
        schema.Schema({"queryCacheSize": str}),
    "/api/user/login":
        schema.Schema({
            "username": str,
            "password": str
        }),
    "/api/user/passwd":
        schema.Schema({
            "username": str,
            "oldPasswd": str,
            "newPasswd": str
        }),
}
