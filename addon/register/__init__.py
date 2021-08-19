
def register_addon():

    from ..menu import register_menu
    from ..operator import register_operator

    register_menu()
    register_operator()


def unregister_addon():

    from ..menu import unregister_menu
    from ..operator import unregister_operator

    unregister_menu()
    unregister_operator()
