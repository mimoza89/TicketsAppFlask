from resources.auth import SignUpResource, SignInResource
routes = (
    (SignUpResource, "/sign-up"),
    (SignInResource, "/sign-in")
)