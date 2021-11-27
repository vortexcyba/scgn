class Messages:
    ADDED_TO_QUEUE = (
        "__Your request has been added to the queue. If you have more than {per_user_process_count}__ "
        "__ongoing processes, then this process will only start after one of them finishes.__"
    )
    MEDIA_MESSAGE_DELETED = "__Why did you delete the file 😠, Now i cannot help you 😒.__"
    CANNOT_OPEN_FILE = "__😟 Sorry! I cannot open the file.__"
    PROCESS_TIMEOUT = (
        "__😟 Sorry! process failed due to timeout. Your process was__ "
        "__taking too long to complete, hence cancelled.__"
    )
    TRACK_USER_ACTIVITY = "User id: `{chat_id}`"
    PROCESSING_REQUEST = "__Processing your request, Please wait! 😴__"
    SCREENSHOT_AT = "__ScreenShot at {time}__"
    SCREENSHOT_PROCESS_FAILED = "__😟 Sorry! Screenshot generation failed possibly due to some infrastructure failure 😥.__"
    SCREENSHOT_PROCESS_SUCCESS = (
        "__🤓 You requested {count} screenshots and__ "
        "__{total_count} screenshots generated,__ "
        "__Now starting to upload!;__"
    )
    PROCESS_UPLOAD_CONFIRM = (
        "__Successfully completed process in {total_process_duration}__\n\n"
        "__Thanks you for using [me](https://t.me/scgnbot).__"
    )
    WRONG_FORMAT = "__Please follow the specified format__"
    VIDEO_PROCESS_CAPTION = "__Sample video. {duration}s from {start}__"
    SCREENSHOTS_START = "__😀 Generating screenshots!.__"

    SAMPLE_VIDEO_PROCESS_START = "__😀 Generating Sample Video! This might take some time.__"
    SAMPLE_VIDEO_PROCESS_FAILED = "__😟 Sorry! Sample video generation failed possibly due to some infrastructure failure 😥.__"
    SAMPLE_VIDEO_PROCESS_SUCCESS = (
        "__🤓 Sample video was generated successfully!, Now starting to upload!__"
    )
    SAMPLE_VIDEO_PROCESS_FAILED_GENERATION = (
        "stream link : {file_link}\n\n duration {sample_duration} sample video "
        "generation failed\n\n{ffmpeg_output}"
    )
    SAMPLE_VIDEO_PROCESS_OPEN_ERROR = (
        "stream link : {file_link}\n\nSample video requested\n\n{duration}"
    )

    SCREENSHOTS_PROGRESS = "😀 `{current}` of `{total}` generated!"
    MANUAL_SCREENSHOTS_OPEN_ERROR = (
        "stream link : {file_link}\n\nRequested manual screenshots\n\n{duration}"
    )
    MANUAL_SCREENSHOTS_NO_VALID_POSITIONS = (
        "__😟 Sorry! None of the given positions where valid!__"
    )
    MANUAL_SCREENSHOTS_VALID_PISITIONS_ABOVE_LIMIT = (
        "__😟 Sorry! Only 10 screenshots can be generated. Found {valid_positions_count}__ "
        "__valid positions in your request__"
    )
    MANUAL_SCREENSHOTS_INVALID_POSITIONS_ALERT = (
        "__Found {invalid_positions_count} invalid positions ({invalid_positions}).__\n\n"
        "__😀 Generating screenshots after ignoring these!.__"
    )
    MANUAL_SCREENSHOTS_FAILED_GENERATION = (
        "stream link : {file_link}\n\nmanual screenshots {raw_user_input}."
    )

    TRIM_VIDEO_INVALID_RANGE = "__The range you provided is invalid!__"
    TRIM_VIDEO_DURATION_ERROR = (
        "__Please provide any range that's upto {max_duration}s.__"
        " __Your requested range **{start}:{end}** is `{request_duration}s` long!__"
    )
    TRIM_VIDEO_OPEN_ERROR = "stream link : {file_link}\n\ntrim video requested\n\n{start}:{end}\n\n{duration}"
    TRIM_VIDEO_RANGE_OUT_OF_VIDEO_DURATION = (
        "__😟 Sorry! The requested range is out of the video's duration!.__"
    )
    TRIM_VIDEO_PROCESS_FAILED = (
        "__😟 Sorry! video trimming failed possibly due to some infrastructure failure 😥.__"
    )
    TRIM_VIDEO_PROCESS_FAILED_GENERATION = "stream link : {file_link}\n\nVideo trim failed.\n\n{start}:{end}\n\n{ffmpeg_output}"
    TRIM_VIDEO_PROCESS_SUCCESS = (
        "__🤓 Video trimmed successfully!, Now starting to upload!__"
    )
    TRIM_VIDEO_START = "__😀 Trimming Your Video! This might take some time.__"

    SCREENSHOTS_OPEN_ERROR = "stream link : {file_link}\n\nRequested screenshots: {num_screenshots}.\n\n{duration}"
    SCREENSHOTS_FAILED_GENERATION = (
        "stream link : {file_link}\n\n{num_screenshots} screenshots where requested "
        "and Screen shots where not generated."
    )

    MEDIAINFO_START = "__Finding the media info, media info will be send here shortly!__"
    SETTINGS = "__Here You can configure my behavior.\n\nPress the button to change the settings.__"
