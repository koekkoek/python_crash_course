def build_profile(first, last, **user_info):
    user_info["First name"] = first
    user_info["Last name"] = last

    return user_info


michel = build_profile(
    "Michel",
    "Koekkoek",
    location="Alphen aan den Rijn",
    hobby="gaming",
    kids=2,
    job="youth pastor",
)

print(michel)
