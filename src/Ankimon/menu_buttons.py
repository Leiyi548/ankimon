from aqt.utils import *
from aqt.qt import *
from PyQt6.QtWidgets import QMenu
from PyQt6.QtGui import QAction, QKeySequence
from aqt import mw  # The main window object
from aqt.utils import qconnect
from .gui_classes.choose_trainer_sprite import TrainerSpriteDialog
from .pyobj.trainer_card_window import TrainerCardGUI
debug = True

# Initialize the menu
mw.pokemenu = QMenu('&Ankimon', mw)
game_menu = mw.pokemenu.addMenu("Game")
profile_menu = mw.pokemenu.addMenu("Profile")
collection_menu = mw.pokemenu.addMenu("Collection")
export_menu = mw.pokemenu.addMenu("Export")
help_menu = mw.pokemenu.addMenu("Help")
if debug is True:
    debug_menu = mw.pokemenu.addMenu("Debug")

def create_menu_actions(
    database_complete,
    online_connectivity,
    pokecollection_win,
    item_window,
    test_window,
    achievement_bag,
    open_team_builder,
    export_to_pkmn_showdown,
    export_all_pkmn_showdown,
    flex_pokemon_collection,
    eff_chart,
    gen_id_chart,
    show_agreement_and_download_database,
    credits,
    license,
    open_help_window,
    report_bug,
    rate_addon_url,
    version_dialog,
    trainer_card,
    ankimon_tracker_window,
    logger,
    data_handler_window,
    settings_window,
    shop_manager,
    pokedex_window,
    ankimon_key,
    join_discord_url,
    settings_obj
):
    actions = []

    if database_complete:
        # Pokémon collection
        pokecol_action = QAction("Show Pokemon Collection", mw)
        collection_menu.addAction(pokecol_action)
        qconnect(pokecol_action.triggered, pokecollection_win.show)

        # Ankimon Window
        ankimon_window_action = QAction("Open Ankimon Window", mw)
        game_menu.addAction(ankimon_window_action)
        ankimon_window_action.setShortcut(QKeySequence(f"{ankimon_key}"))
        qconnect(ankimon_window_action.triggered, test_window.open_dynamic_window)

        # Itembag
        itembag_action = QAction("Itembag", mw)
        itembag_action.triggered.connect(item_window.show_window)
        collection_menu.addAction(itembag_action)

        # Achievements
        achievement_bag_action = QAction("Achievements", mw)
        achievement_bag_action.triggered.connect(achievement_bag.show_window)
        profile_menu.addAction(achievement_bag_action)

        # Showdown Teambuilder
        pokemon_showdown_action = QAction("Open Pokemon Showdown Teambuilder", mw)
        qconnect(pokemon_showdown_action.triggered, open_team_builder)
        export_menu.addAction(pokemon_showdown_action)

        # Export to Showdown
        export_main_to_showdown = QAction("Export Main Pokemon to PkmnShowdown", mw)
        qconnect(export_main_to_showdown.triggered, export_to_pkmn_showdown)
        export_menu.addAction(export_main_to_showdown)

        export_all_to_showdown = QAction("Export All Pokemon to PkmnShowdown", mw)
        qconnect(export_all_to_showdown.triggered, export_all_pkmn_showdown)
        export_menu.addAction(export_all_to_showdown)

        # Flexing Collection
        flex_pokecoll_action = QAction("Export All Pokemon to PokePast for flexing", mw)
        qconnect(flex_pokecoll_action.triggered, flex_pokemon_collection)
        export_menu.addAction(flex_pokecoll_action)

        pokedex_action = QAction("Open Pokedex", mw)
        qconnect(pokedex_action.triggered, pokedex_window.show)
        collection_menu.addAction(pokedex_action)

    # Effectiveness chart
    eff_chart_action = QAction("Check Effectiveness Chart", mw)
    eff_chart_action.triggered.connect(eff_chart.show_eff_chart)
    help_menu.addAction(eff_chart_action)

    # Generations and Pokémon chart
    gen_and_poke_chart_action = QAction("Check Generations and Pokemon Chart", mw)
    gen_and_poke_chart_action.triggered.connect(gen_id_chart.show_gen_chart)
    help_menu.addAction(gen_and_poke_chart_action)

    # Effectiveness chart
    join_discord_action = QAction("Join Discord Channel", mw)
    join_discord_action.triggered.connect(join_discord_url)
    help_menu.addAction(join_discord_action)

    # Download Resources
    test_action3 = QAction("Download Resources", mw)
    qconnect(test_action3.triggered, show_agreement_and_download_database)
    mw.pokemenu.addAction(test_action3)

    # Credits
    credits_action = QAction("Credits", mw)
    credits_action.triggered.connect(credits.show_window)
    help_menu.addAction(credits_action)

    # About and License
    about_and_license_action = QAction("About and License", mw)
    about_and_license_action.triggered.connect(license.show_window)
    help_menu.addAction(about_and_license_action)

    # Help Guide
    help_action = QAction("Open Help Guide", mw)
    help_action.triggered.connect(lambda: open_help_window(online_connectivity))
    help_menu.addAction(help_action)

    # Report Bug
    report_bug_action = QAction("Report Bug", mw)
    report_bug_action.triggered.connect(report_bug)
    help_menu.addAction(report_bug_action)

    # Rate Addon
    rate_action = QAction("Rate This", mw)
    rate_action.triggered.connect(rate_addon_url)
    mw.pokemenu.addAction(rate_action)

    # Version
    version_action = QAction("Version", mw)
    version_action.triggered.connect(version_dialog.open)
    help_menu.addAction(version_action)

    config_action = QAction("Settings", mw)
    config_action.triggered.connect(settings_window.show_window)
    # Show the Settings window
    mw.pokemenu.addAction(config_action)

    if debug is True:
        data_window_action = QAction("Data", mw)
        data_window_action.triggered.connect(data_handler_window.show_window)
        # Show the Settings window
        debug_menu.addAction(data_window_action)

        tracker_window_action = QAction("Tracker", mw)
        tracker_window_action.triggered.connect(ankimon_tracker_window.toggle_window)
        tracker_window_action.setShortcut(QKeySequence("Ctrl+Shift+K"))
        # Show the Settings window
        debug_menu.addAction(tracker_window_action)

    # Set up a shortcut (Ctrl+Shift+L) to open the log window
    ankimon_logger_action = QAction("Logger", mw)
    ankimon_logger_action.setShortcut(QKeySequence("Ctrl+Shift+L"))
    ankimon_logger_action.triggered.connect(logger.toggle_log_window)
    game_menu.addAction(ankimon_logger_action)

    # Set up a shortcut (Ctrl+L) to open the log window
    ankimon_trainer_card_action = QAction("Trainer Card", mw)
    ankimon_trainer_card_action.setShortcut(QKeySequence("Ctrl+Shift+Q"))
    # Create the TrainerCard GUI and show it inside Anki's main window
    ankimon_trainer_card_action.triggered.connect(lambda: TrainerCardGUI(trainer_card, settings_obj, parent=mw))
    profile_menu.addAction(ankimon_trainer_card_action)

    # Add AnkimonShop Action to toggle the shop
    shop_manager_action = QAction("Item Shop", mw)
    shop_manager_action.triggered.connect(shop_manager.toggle_window)
    game_menu.addAction(shop_manager_action)

    # Choose Trainer Sprite Action
    choose_trainer_sprite_action = QAction("Choose trainer sprite", mw)
    choose_trainer_sprite_action.triggered.connect(lambda: TrainerSpriteDialog(settings_obj=settings_obj).exec())
    game_menu.addAction(choose_trainer_sprite_action)

    mw.form.menubar.addMenu(mw.pokemenu)