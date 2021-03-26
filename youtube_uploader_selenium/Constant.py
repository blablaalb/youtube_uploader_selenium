class Constant:
    """A class for storing constants for YoutubeUploader class"""
    YOUTUBE_URL = 'https://www.youtube.com'
    YOUTUBE_STUDIO_URL = 'https://studio.youtube.com'
    YOUTUBE_UPLOAD_URL = 'https://www.youtube.com/upload'
    USER_WAITING_TIME = 1
    VIDEO_TITLE = 'title'
    VIDEO_DESCRIPTION = 'description'
    VIDEO_TAGS = 'tags'
    # DESCRIPTION_CONTAINER = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/' \
    # 'ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]'
    DESCRIPTION_CONTAINER = '//*[@id="details" and @class="style-scope ytcp-uploads-dialog"]'
    TEXTBOX = 'textbox'
    TEXT_INPUT = 'text-input'
    RADIO_LABEL = 'radioLabel'
    STATUS_CONTAINER = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/' \
                       'div/div[1]/ytcp-video-upload-progress/span'
    NOT_MADE_FOR_KIDS_LABEL = 'NOT_MADE_FOR_KIDS'
    # MORE_BUTTON = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/div/ytcp-button'
    MORE_BUTTON = '//*[@id="toggle-button"]'
    TAGS_INPUT_CONTAINER = '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-advanced/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div'
    # TAGS_INPUT = 'text-input'
    TAGS_INPUT = '//*[@id="text-input" and @aria-label="Tags"]'
    NEXT_BUTTON = 'next-button'
    #PUBLIC_BUTTON = 'PUBLIC'
    PUBLIC_BUTTON = '//*[@id="privacy-radios"]/*[@name="PUBLIC"]'
    VIDEO_URL_CONTAINER = "//span[@class='video-url-fadeable style-scope ytcp-video-info']"
    VIDEO_URL_ELEMENT = "//a[@class='style-scope ytcp-video-info']"
    HREF = 'href'
    UPLOADED = 'Uploading'
    ERROR_CONTAINER = '//*[@id="error-message"]'
    VIDEO_NOT_FOUND_ERROR = 'Could not find video_id'
    DONE_BUTTON = 'done-button'
    INPUT_FILE_VIDEO = "//input[@type='file']"
    INPUT_FILE_THUMBNAIL = "//input[@id='file-loader']"
