from django.contrib.auth import get_user_model


Account = get_user_model()


# @receiver(post_save, sender=Account)
# def create_cart(sender, instance, created, **kwargs):
#     if created:
#         #check sessionid and create cart for user
#         Cart.objects.create(user=instance) # request.user

# TODO Create cart in Register view