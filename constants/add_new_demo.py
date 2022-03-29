class AddNewDemo:
    """GAME INFORMATION"""
    DEMO_NAME_XPATH = ".//input[@type='text' and @id='demo_demoName']"
    '''DEMO LINKS'''
    LANGUAGE_XPATH = ".//select[@id='demo_links_0_language']"
    ACTIVE_CHECKBOX_XPATH = ".//input[@type='checkbox' and @id='demo_links_0_isActive']"
    REPLACE_CHECKBOX_XPATH = ".//input[@type='checkbox' and @id='demo_links_0_replacement']"
    HTML_TEXT_AREA_XPATH = ".//textarea[@id='demo_links_0_html']"
    MOBILE_HTML_TEXT_AREA_XPATH = ".//textarea[@id='demo_links_0_mobileHtml']"
    '''FEATURES'''
    """FREE_SPINS_XPATH =
    RISK_GAME_XPATH =
    SOUND_XPATH =
    AUTO_GAME_XPATH =
    BONUS_ROUNDS_XPATH =
    SCATTER_SYMBOL_XPATH =
    WILD_SYMBOL_XPATH =
    MULTIPLIER_XPATH ="""

    REELS_AMOUNT_XPATH = ".//input[@id='demo_drumsAmount']"
    MIN_RATE_XPATH = ".//input[@id='demo_minRate']"
    RTP_XPATH = ".//input[@id='demo_rtp']"
    LINES_AMOUNT_XPATH = ".//input[@id='demo_linesAmount']"
    MAX_RATE_XPATH = ".//input[@id='demo_maxRate']"
    JACKPOT_XPATH = ".//input[@id='demo_jackpot']"
    POPULARITY_XPATH = ".//input[@id='demo_popularity']"
    RELEASE_DATE_XPATH = ".//input[@id='demo_releaseDate']"

    """IMAGES"""
    LOGO_SELECT_FILE_XPATH = ".//input[@type='file' and @id='demo_imageFile']"
    SCREENSHOTS_SELECT_FILE_XPATH = ".//input[@type='file' and @id='demo_screenshotFile']"
    SAVE_BUTTON_XPATH = ".//button[@class='btn btn-success']"
    TO_LIST_BUTTON_XPATH = ".//a[@class='btn btn-primary ml-2']"
