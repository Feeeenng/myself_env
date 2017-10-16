# encoding: utf-8
# module win32comext.shell.shell
# from D:\ProgramData\Anaconda3\lib\site-packages\win32comext\shell\shell.pyd
# by generator 1.145
""" A module wrapping Windows Shell functions and interfaces """

# imports
from pywintypes import error


# Variables with simple values

HOTKEYF_ALT = 4
HOTKEYF_CONTROL = 2
HOTKEYF_EXT = 8
HOTKEYF_SHIFT = 1

SLGP_RAWPATH = 4
SLGP_SHORTPATH = 1
SLGP_UNCPRIORITY = 2

SLR_ANY_MATCH = 2

SLR_INVOKE_MSI = 128

SLR_NOLINKINFO = 64
SLR_NOSEARCH = 16
SLR_NOTRACK = 32
SLR_NOUPDATE = 8

SLR_NO_UI = 1

SLR_UPDATE = 4

# functions

def AddressAsPIDL(*args, **kwargs): # real signature unknown
    pass

def AssocCreate(*args, **kwargs): # real signature unknown
    pass

def AssocCreateForClasses(*args, **kwargs): # real signature unknown
    pass

def CIDAAsString(*args, **kwargs): # real signature unknown
    pass

def DragQueryFile(*args, **kwargs): # real signature unknown
    pass

def DragQueryFileW(*args, **kwargs): # real signature unknown
    pass

def DragQueryPoint(*args, **kwargs): # real signature unknown
    pass

def FILEGROUPDESCRIPTORAsString(*args, **kwargs): # real signature unknown
    pass

def GetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    pass

def IsUserAnAdmin(*args, **kwargs): # real signature unknown
    pass

def PIDLAsString(*args, **kwargs): # real signature unknown
    pass

def SetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    pass

def SHAddToRecentDocs(*args, **kwargs): # real signature unknown
    pass

def SHBrowseForFolder(*args, **kwargs): # real signature unknown
    pass

def SHChangeNotify(*args, **kwargs): # real signature unknown
    pass

def SHChangeNotifyDeregister(*args, **kwargs): # real signature unknown
    pass

def SHChangeNotifyRegister(*args, **kwargs): # real signature unknown
    pass

def SHCreateDataObject(*args, **kwargs): # real signature unknown
    pass

def SHCreateDefaultContextMenu(*args, **kwargs): # real signature unknown
    pass

def SHCreateDefaultExtractIcon(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemFromIDList(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemFromParsingName(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemFromRelativeName(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemInKnownFolder(*args, **kwargs): # real signature unknown
    pass

def SHCreateItemWithParent(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellFolderView(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItem(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArray(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArrayFromDataObject(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArrayFromIDLists(*args, **kwargs): # real signature unknown
    pass

def SHCreateShellItemArrayFromShellItem(*args, **kwargs): # real signature unknown
    pass

def SHCreateStreamOnFileEx(*args, **kwargs): # real signature unknown
    pass

def ShellExecuteEx(*args, **kwargs): # real signature unknown
    pass

def SHEmptyRecycleBin(*args, **kwargs): # real signature unknown
    pass

def SHFileOperation(*args, **kwargs): # real signature unknown
    pass

def SHGetDesktopFolder(*args, **kwargs): # real signature unknown
    pass

def SHGetFileInfo(*args, **kwargs): # real signature unknown
    pass

def SHGetFolderLocation(*args, **kwargs): # real signature unknown
    pass

def SHGetFolderPath(*args, **kwargs): # real signature unknown
    pass

def SHGetIDListFromObject(*args, **kwargs): # real signature unknown
    pass

def SHGetInstanceExplorer(*args, **kwargs): # real signature unknown
    pass

def SHGetNameFromIDList(*args, **kwargs): # real signature unknown
    pass

def SHGetPathFromIDList(*args, **kwargs): # real signature unknown
    pass

def SHGetPathFromIDListW(*args, **kwargs): # real signature unknown
    pass

def SHGetSettings(*args, **kwargs): # real signature unknown
    pass

def SHGetSpecialFolderLocation(*args, **kwargs): # real signature unknown
    pass

def SHGetSpecialFolderPath(*args, **kwargs): # real signature unknown
    pass

def SHGetViewStatePropertyBag(*args, **kwargs): # real signature unknown
    pass

def SHILCreateFromPath(*args, **kwargs): # real signature unknown
    pass

def SHOpenFolderAndSelectItems(*args, **kwargs): # real signature unknown
    pass

def SHParseDisplayName(*args, **kwargs): # real signature unknown
    pass

def SHQueryRecycleBin(*args, **kwargs): # real signature unknown
    pass

def SHSetFolderPath(*args, **kwargs): # real signature unknown
    pass

def SHUpdateImage(*args, **kwargs): # real signature unknown
    pass

def StringAsCIDA(*args, **kwargs): # real signature unknown
    pass

def StringAsFILEGROUPDESCRIPTOR(*args, **kwargs): # real signature unknown
    pass

def StringAsPIDL(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

BHID_AssociationArray = None # (!) real value is ''

BHID_DataObject = None # (!) real value is ''

BHID_EnumItems = None # (!) real value is ''

BHID_Filter = None # (!) real value is ''

BHID_LinkTargetItem = None # (!) real value is ''

BHID_PropertyStore = None # (!) real value is ''

BHID_SFObject = None # (!) real value is ''

BHID_SFUIObject = None # (!) real value is ''

BHID_SFViewObject = None # (!) real value is ''

BHID_Storage = None # (!) real value is ''

BHID_StorageEnum = None # (!) real value is ''

BHID_Stream = None # (!) real value is ''

BHID_ThumbnailHandler = None # (!) real value is ''

BHID_Transfer = None # (!) real value is ''

CGID_DefView = None # (!) real value is ''

CGID_Explorer = None # (!) real value is ''

CGID_ExplorerBarDoc = None # (!) real value is ''

CGID_ShellDocView = None # (!) real value is ''

CGID_ShellServiceObject = None # (!) real value is ''

CLSID_ActiveDesktop = None # (!) real value is ''

CLSID_ApplicationDestinations = None # (!) real value is ''

CLSID_ApplicationDocumentLists = None # (!) real value is ''

CLSID_ControlPanel = None # (!) real value is ''

CLSID_DestinationList = None # (!) real value is ''

CLSID_DragDropHelper = None # (!) real value is ''

CLSID_EnumerableObjectCollection = None # (!) real value is ''

CLSID_FileOperation = None # (!) real value is ''

CLSID_Internet = None # (!) real value is ''

CLSID_InternetShortcut = None # (!) real value is ''

CLSID_KnownFolderManager = None # (!) real value is ''

CLSID_MyComputer = None # (!) real value is ''

CLSID_MyDocuments = None # (!) real value is ''

CLSID_NetworkDomain = None # (!) real value is ''

CLSID_NetworkPlaces = None # (!) real value is ''

CLSID_NetworkServer = None # (!) real value is ''

CLSID_NetworkShare = None # (!) real value is ''

CLSID_Printers = None # (!) real value is ''

CLSID_RecycleBin = None # (!) real value is ''

CLSID_ShellDesktop = None # (!) real value is ''

CLSID_ShellFSFolder = None # (!) real value is ''

CLSID_ShellItem = None # (!) real value is ''

CLSID_ShellLibrary = None # (!) real value is ''

CLSID_ShellLink = None # (!) real value is ''

CLSID_TaskbarList = None # (!) real value is ''

EP_AdvQueryPane = None # (!) real value is ''

EP_Commands = None # (!) real value is ''

EP_Commands_Organize = None # (!) real value is ''

EP_Commands_View = None # (!) real value is ''

EP_DetailsPane = None # (!) real value is ''

EP_NavPane = None # (!) real value is ''

EP_PreviewPane = None # (!) real value is ''

EP_QueryPane = None # (!) real value is ''

FMTID_AudioSummaryInformation = None # (!) real value is ''

FMTID_Briefcase = None # (!) real value is ''

FMTID_Displaced = None # (!) real value is ''

FMTID_ImageProperties = None # (!) real value is ''

FMTID_ImageSummaryInformation = None # (!) real value is ''

FMTID_InternetSite = None # (!) real value is ''

FMTID_Intshcut = None # (!) real value is ''

FMTID_MediaFileSummaryInformation = None # (!) real value is ''

FMTID_Misc = None # (!) real value is ''

FMTID_Query = None # (!) real value is ''

FMTID_ShellDetails = None # (!) real value is ''

FMTID_Storage = None # (!) real value is ''

FMTID_SummaryInformation = None # (!) real value is ''

FMTID_Volume = None # (!) real value is ''

FMTID_WebView = None # (!) real value is ''

FOLDERID_AddNewPrograms = None # (!) real value is ''

FOLDERID_AdminTools = None # (!) real value is ''

FOLDERID_AppUpdates = None # (!) real value is ''

FOLDERID_CDBurning = None # (!) real value is ''

FOLDERID_ChangeRemovePrograms = None # (!) real value is ''

FOLDERID_CommonAdminTools = None # (!) real value is ''

FOLDERID_CommonOEMLinks = None # (!) real value is ''

FOLDERID_CommonPrograms = None # (!) real value is ''

FOLDERID_CommonStartMenu = None # (!) real value is ''

FOLDERID_CommonStartup = None # (!) real value is ''

FOLDERID_CommonTemplates = None # (!) real value is ''

FOLDERID_ComputerFolder = None # (!) real value is ''

FOLDERID_ConflictFolder = None # (!) real value is ''

FOLDERID_ConnectionsFolder = None # (!) real value is ''

FOLDERID_Contacts = None # (!) real value is ''

FOLDERID_ControlPanelFolder = None # (!) real value is ''

FOLDERID_Cookies = None # (!) real value is ''

FOLDERID_Desktop = None # (!) real value is ''

FOLDERID_DeviceMetadataStore = None # (!) real value is ''

FOLDERID_Documents = None # (!) real value is ''

FOLDERID_DocumentsLibrary = None # (!) real value is ''

FOLDERID_Downloads = None # (!) real value is ''

FOLDERID_Favorites = None # (!) real value is ''

FOLDERID_Fonts = None # (!) real value is ''

FOLDERID_Games = None # (!) real value is ''

FOLDERID_GameTasks = None # (!) real value is ''

FOLDERID_History = None # (!) real value is ''

FOLDERID_HomeGroup = None # (!) real value is ''

FOLDERID_ImplicitAppShortcuts = None # (!) real value is ''

FOLDERID_InternetCache = None # (!) real value is ''

FOLDERID_InternetFolder = None # (!) real value is ''

FOLDERID_Libraries = None # (!) real value is ''

FOLDERID_Links = None # (!) real value is ''

FOLDERID_LocalAppData = None # (!) real value is ''

FOLDERID_LocalAppDataLow = None # (!) real value is ''

FOLDERID_LocalizedResourcesDir = None # (!) real value is ''

FOLDERID_Music = None # (!) real value is ''

FOLDERID_MusicLibrary = None # (!) real value is ''

FOLDERID_NetHood = None # (!) real value is ''

FOLDERID_NetworkFolder = None # (!) real value is ''

FOLDERID_OriginalImages = None # (!) real value is ''

FOLDERID_PhotoAlbums = None # (!) real value is ''

FOLDERID_Pictures = None # (!) real value is ''

FOLDERID_PicturesLibrary = None # (!) real value is ''

FOLDERID_Playlists = None # (!) real value is ''

FOLDERID_PrintersFolder = None # (!) real value is ''

FOLDERID_PrintHood = None # (!) real value is ''

FOLDERID_Profile = None # (!) real value is ''

FOLDERID_ProgramData = None # (!) real value is ''

FOLDERID_ProgramFiles = None # (!) real value is ''

FOLDERID_ProgramFilesCommon = None # (!) real value is ''

FOLDERID_ProgramFilesCommonX64 = None # (!) real value is ''

FOLDERID_ProgramFilesCommonX86 = None # (!) real value is ''

FOLDERID_ProgramFilesX64 = None # (!) real value is ''

FOLDERID_ProgramFilesX86 = None # (!) real value is ''

FOLDERID_Programs = None # (!) real value is ''

FOLDERID_Public = None # (!) real value is ''

FOLDERID_PublicDesktop = None # (!) real value is ''

FOLDERID_PublicDocuments = None # (!) real value is ''

FOLDERID_PublicDownloads = None # (!) real value is ''

FOLDERID_PublicGameTasks = None # (!) real value is ''

FOLDERID_PublicLibraries = None # (!) real value is ''

FOLDERID_PublicMusic = None # (!) real value is ''

FOLDERID_PublicPictures = None # (!) real value is ''

FOLDERID_PublicRingtones = None # (!) real value is ''

FOLDERID_PublicVideos = None # (!) real value is ''

FOLDERID_QuickLaunch = None # (!) real value is ''

FOLDERID_Recent = None # (!) real value is ''

FOLDERID_RecordedTVLibrary = None # (!) real value is ''

FOLDERID_RecycleBinFolder = None # (!) real value is ''

FOLDERID_ResourceDir = None # (!) real value is ''

FOLDERID_Ringtones = None # (!) real value is ''

FOLDERID_RoamingAppData = None # (!) real value is ''

FOLDERID_SampleMusic = None # (!) real value is ''

FOLDERID_SamplePictures = None # (!) real value is ''

FOLDERID_SamplePlaylists = None # (!) real value is ''

FOLDERID_SampleVideos = None # (!) real value is ''

FOLDERID_SavedGames = None # (!) real value is ''

FOLDERID_SavedSearches = None # (!) real value is ''

FOLDERID_SearchHome = None # (!) real value is ''

FOLDERID_SEARCH_CSC = None # (!) real value is ''

FOLDERID_SEARCH_MAPI = None # (!) real value is ''

FOLDERID_SendTo = None # (!) real value is ''

FOLDERID_SidebarDefaultParts = None # (!) real value is ''

FOLDERID_SidebarParts = None # (!) real value is ''

FOLDERID_StartMenu = None # (!) real value is ''

FOLDERID_Startup = None # (!) real value is ''

FOLDERID_SyncManagerFolder = None # (!) real value is ''

FOLDERID_SyncResultsFolder = None # (!) real value is ''

FOLDERID_SyncSetupFolder = None # (!) real value is ''

FOLDERID_System = None # (!) real value is ''

FOLDERID_SystemX86 = None # (!) real value is ''

FOLDERID_Templates = None # (!) real value is ''

FOLDERID_UserPinned = None # (!) real value is ''

FOLDERID_UserProfiles = None # (!) real value is ''

FOLDERID_UserProgramFiles = None # (!) real value is ''

FOLDERID_UserProgramFilesCommon = None # (!) real value is ''

FOLDERID_UsersFiles = None # (!) real value is ''

FOLDERID_UsersLibraries = None # (!) real value is ''

FOLDERID_Videos = None # (!) real value is ''

FOLDERID_VideosLibrary = None # (!) real value is ''

FOLDERID_Windows = None # (!) real value is ''

FOLDERTYPEID_Communications = None # (!) real value is ''

FOLDERTYPEID_CompressedFolder = None # (!) real value is ''

FOLDERTYPEID_Contacts = None # (!) real value is ''

FOLDERTYPEID_ControlPanelCategory = None # (!) real value is ''

FOLDERTYPEID_ControlPanelClassic = None # (!) real value is ''

FOLDERTYPEID_Documents = None # (!) real value is ''

FOLDERTYPEID_Games = None # (!) real value is ''

FOLDERTYPEID_Generic = None # (!) real value is ''

FOLDERTYPEID_GenericLibrary = None # (!) real value is ''

FOLDERTYPEID_GenericSearchResults = None # (!) real value is ''

FOLDERTYPEID_Invalid = None # (!) real value is ''

FOLDERTYPEID_Music = None # (!) real value is ''

FOLDERTYPEID_NetworkExplorer = None # (!) real value is ''

FOLDERTYPEID_OpenSearch = None # (!) real value is ''

FOLDERTYPEID_OtherUsers = None # (!) real value is ''

FOLDERTYPEID_Pictures = None # (!) real value is ''

FOLDERTYPEID_Printers = None # (!) real value is ''

FOLDERTYPEID_PublishedItems = None # (!) real value is ''

FOLDERTYPEID_RecordedTV = None # (!) real value is ''

FOLDERTYPEID_RecycleBin = None # (!) real value is ''

FOLDERTYPEID_SavedGames = None # (!) real value is ''

FOLDERTYPEID_SearchConnector = None # (!) real value is ''

FOLDERTYPEID_Searches = None # (!) real value is ''

FOLDERTYPEID_SearchHome = None # (!) real value is ''

FOLDERTYPEID_SoftwareExplorer = None # (!) real value is ''

FOLDERTYPEID_StartMenu = None # (!) real value is ''

FOLDERTYPEID_UserFiles = None # (!) real value is ''

FOLDERTYPEID_UsersLibraries = None # (!) real value is ''

FOLDERTYPEID_Videos = None # (!) real value is ''

IID_CDefView = None # (!) real value is ''

IID_IActiveDesktop = None # (!) real value is ''

IID_IActiveDesktopP = None # (!) real value is ''

IID_IADesktopP2 = None # (!) real value is ''

IID_IApplicationDestinations = None # (!) real value is ''

IID_IApplicationDocumentLists = None # (!) real value is ''

IID_IAsyncOperation = None # (!) real value is ''

IID_IBrowserFrameOptions = None # (!) real value is ''

IID_ICategorizer = None # (!) real value is ''

IID_ICategoryProvider = None # (!) real value is ''

IID_IColumnProvider = None # (!) real value is ''

IID_IContextMenu = None # (!) real value is ''

IID_IContextMenu2 = None # (!) real value is ''

IID_IContextMenu3 = None # (!) real value is ''

IID_ICopyHook = None # (!) real value is ''

IID_ICopyHookA = None # (!) real value is ''

IID_ICopyHookW = None # (!) real value is ''

IID_ICurrentItem = None # (!) real value is ''

IID_ICustomDestinationList = None # (!) real value is ''

IID_IDefaultExtractIconInit = None # (!) real value is ''

IID_IDeskBand = None # (!) real value is ''

IID_IDisplayItem = None # (!) real value is ''

IID_IDockingWindow = None # (!) real value is ''

IID_IDropTargetHelper = None # (!) real value is ''

IID_IEmptyVolumeCache = None # (!) real value is ''

IID_IEmptyVolumeCache2 = None # (!) real value is ''

IID_IEmptyVolumeCacheCallBack = None # (!) real value is ''

IID_IEnumExplorerCommand = None # (!) real value is ''

IID_IEnumIDList = None # (!) real value is ''

IID_IEnumObjects = None # (!) real value is ''

IID_IEnumResources = None # (!) real value is ''

IID_IEnumShellItems = None # (!) real value is ''

IID_IExplorerBrowser = None # (!) real value is ''

IID_IExplorerBrowserEvents = None # (!) real value is ''

IID_IExplorerCommand = None # (!) real value is ''

IID_IExplorerCommandProvider = None # (!) real value is ''

IID_IExplorerPaneVisibility = None # (!) real value is ''

IID_IExtractIcon = None # (!) real value is ''

IID_IExtractIconW = None # (!) real value is ''

IID_IExtractImage = None # (!) real value is ''

IID_IFileOperation = None # (!) real value is ''

IID_IFileOperationProgressSink = None # (!) real value is ''

IID_IIdentityName = None # (!) real value is ''

IID_IKnownFolder = None # (!) real value is ''

IID_IKnownFolderManager = None # (!) real value is ''

IID_INameSpaceTreeControl = None # (!) real value is ''

IID_IObjectArray = None # (!) real value is ''

IID_IObjectCollection = None # (!) real value is ''

IID_IPersistFolder = None # (!) real value is ''

IID_IPersistFolder2 = None # (!) real value is ''

IID_IQueryAssociations = None # (!) real value is ''

IID_IRelatedItem = None # (!) real value is ''

IID_IShellBrowser = None # (!) real value is ''

IID_IShellCopyHook = None # (!) real value is ''

IID_IShellCopyHookA = None # (!) real value is ''

IID_IShellCopyHookW = None # (!) real value is ''

IID_IShellExtInit = None # (!) real value is ''

IID_IShellFolder = None # (!) real value is ''

IID_IShellFolder2 = None # (!) real value is ''

IID_IShellIcon = None # (!) real value is ''

IID_IShellIconOverlay = None # (!) real value is ''

IID_IShellIconOverlayIdentifier = None # (!) real value is ''

IID_IShellIconOverlayManager = None # (!) real value is ''

IID_IShellItem = None # (!) real value is ''

IID_IShellItem2 = None # (!) real value is ''

IID_IShellItemArray = None # (!) real value is ''

IID_IShellItemResources = None # (!) real value is ''

IID_IShellLibrary = None # (!) real value is ''

IID_IShellLink = None # (!) real value is ''

IID_IShellLinkA = None # (!) real value is ''

IID_IShellLinkDataList = None # (!) real value is ''

IID_IShellLinkW = None # (!) real value is ''

IID_IShellView = None # (!) real value is ''

IID_ITaskbarList = None # (!) real value is ''

IID_ITransferAdviseSink = None # (!) real value is ''

IID_ITransferDestination = None # (!) real value is ''

IID_ITransferMediumItem = None # (!) real value is ''

IID_ITransferSource = None # (!) real value is ''

IID_IUniformResourceLocator = None # (!) real value is ''

ResourceTypeStream = None # (!) real value is ''

SID_CtxQueryAssociations = None # (!) real value is ''

SID_DefView = None # (!) real value is ''

SID_LinkSite = None # (!) real value is ''

SID_MenuShellFolder = None # (!) real value is ''

SID_SCommDlgBrowser = None # (!) real value is ''

SID_SGetViewFromViewDual = None # (!) real value is ''

SID_ShellFolderViewCB = None # (!) real value is ''

SID_SInternetExplorer = None # (!) real value is ''

SID_SMenuBandBKContextMenu = None # (!) real value is ''

SID_SMenuBandBottom = None # (!) real value is ''

SID_SMenuBandBottomSelected = None # (!) real value is ''

SID_SMenuBandChild = None # (!) real value is ''

SID_SMenuBandContextMenuModifier = None # (!) real value is ''

SID_SMenuBandParent = None # (!) real value is ''

SID_SMenuBandTop = None # (!) real value is ''

SID_SMenuPopup = None # (!) real value is ''

SID_SProgressUI = None # (!) real value is ''

SID_SShellBrowser = None # (!) real value is ''

SID_SShellDesktop = None # (!) real value is ''

SID_STopLevelBrowser = None # (!) real value is ''

SID_STopWindow = None # (!) real value is ''

SID_SUrlHistory = None # (!) real value is ''

SID_SWebBrowserApp = None # (!) real value is ''

VID_Details = None # (!) real value is ''

VID_LargeIcons = None # (!) real value is ''

VID_List = None # (!) real value is ''

VID_SmallIcons = None # (!) real value is ''

VID_Thumbnails = None # (!) real value is ''

VID_ThumbStrip = None # (!) real value is ''

VID_Tile = None # (!) real value is ''

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

