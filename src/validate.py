import schema

schemas = {
    "/api/admin/login": schema.Schema({
        "username": str,
        "passwd": str
    }),
}
