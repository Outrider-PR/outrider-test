from flask import redirect, request


def go_next():
    target = request.args.get("next", "/")
    return redirect(target)


def admin_redirect(user):
    if not user.get("is_admin"):
        return redirect("/login")
    dest = request.args.get("return_to", "/admin")
    return redirect(dest)
