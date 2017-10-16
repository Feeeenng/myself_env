# encoding: utf-8
# module PyQt5.QtBluetooth
# from D:\ProgramData\Anaconda3\lib\site-packages\PyQt5\QtBluetooth.pyd
# by generator 1.145
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# no functions
# classes

class QBluetooth(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Authentication = 2
    Authorization = 1
    Encryption = 4
    NoSecurity = 0
    Secure = 8


class QBluetoothAddress(): # skipped bases: <class 'sip.wrapper'>
    """
    QBluetoothAddress()
    QBluetoothAddress(int)
    QBluetoothAddress(str)
    QBluetoothAddress(QBluetoothAddress)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def toUInt64(self): # real signature unknown; restored from __doc__
        """ toUInt64(self) -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QBluetoothDeviceDiscoveryAgent(__PyQt5_QtCore.QObject):
    """
    QBluetoothDeviceDiscoveryAgent(parent: QObject = None)
    QBluetoothDeviceDiscoveryAgent(QBluetoothAddress, parent: QObject = None)
    """
    def canceled(self): # real signature unknown; restored from __doc__
        """ canceled(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deviceDiscovered(self, QBluetoothDeviceInfo): # real signature unknown; restored from __doc__
        """ deviceDiscovered(self, QBluetoothDeviceInfo) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def discoveredDevices(self): # real signature unknown; restored from __doc__
        """ discoveredDevices(self) -> object """
        return object()

    def error(self, QBluetoothDeviceDiscoveryAgent_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QBluetoothDeviceDiscoveryAgent.Error
        error(self, QBluetoothDeviceDiscoveryAgent.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def inquiryType(self): # real signature unknown; restored from __doc__
        """ inquiryType(self) -> QBluetoothDeviceDiscoveryAgent.InquiryType """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInquiryType(self, QBluetoothDeviceDiscoveryAgent_InquiryType): # real signature unknown; restored from __doc__
        """ setInquiryType(self, QBluetoothDeviceDiscoveryAgent.InquiryType) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    GeneralUnlimitedInquiry = 0
    InputOutputError = 1
    InvalidBluetoothAdapterError = 3
    LimitedInquiry = 1
    NoError = 0
    PoweredOffError = 2
    UnknownError = 100
    UnsupportedPlatformError = 4


class QBluetoothDeviceInfo(): # skipped bases: <class 'sip.wrapper'>
    """
    QBluetoothDeviceInfo()
    QBluetoothDeviceInfo(QBluetoothAddress, str, int)
    QBluetoothDeviceInfo(QBluetoothUuid, str, int)
    QBluetoothDeviceInfo(QBluetoothDeviceInfo)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def coreConfigurations(self): # real signature unknown; restored from __doc__
        """ coreConfigurations(self) -> QBluetoothDeviceInfo.CoreConfigurations """
        pass

    def deviceUuid(self): # real signature unknown; restored from __doc__
        """ deviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def isCached(self): # real signature unknown; restored from __doc__
        """ isCached(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def majorDeviceClass(self): # real signature unknown; restored from __doc__
        """ majorDeviceClass(self) -> QBluetoothDeviceInfo.MajorDeviceClass """
        pass

    def minorDeviceClass(self): # real signature unknown; restored from __doc__
        """ minorDeviceClass(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def rssi(self): # real signature unknown; restored from __doc__
        """ rssi(self) -> int """
        return 0

    def serviceClasses(self): # real signature unknown; restored from __doc__
        """ serviceClasses(self) -> QBluetoothDeviceInfo.ServiceClasses """
        pass

    def serviceUuids(self): # real signature unknown; restored from __doc__
        """ serviceUuids(self) -> Tuple[List[QBluetoothUuid], QBluetoothDeviceInfo.DataCompleteness] """
        pass

    def serviceUuidsCompleteness(self): # real signature unknown; restored from __doc__
        """ serviceUuidsCompleteness(self) -> QBluetoothDeviceInfo.DataCompleteness """
        pass

    def setCached(self, bool): # real signature unknown; restored from __doc__
        """ setCached(self, bool) """
        pass

    def setCoreConfigurations(self, QBluetoothDeviceInfo_CoreConfigurations): # real signature unknown; restored from __doc__
        """ setCoreConfigurations(self, QBluetoothDeviceInfo.CoreConfigurations) """
        pass

    def setDeviceUuid(self, QBluetoothUuid): # real signature unknown; restored from __doc__
        """ setDeviceUuid(self, QBluetoothUuid) """
        pass

    def setRssi(self, p_int): # real signature unknown; restored from __doc__
        """ setRssi(self, int) """
        pass

    def setServiceUuids(self, p_object, QBluetoothDeviceInfo_DataCompleteness): # real signature unknown; restored from __doc__
        """ setServiceUuids(self, object, QBluetoothDeviceInfo.DataCompleteness) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AllServices = 2047
    AudioService = 32
    AudioVideoDevice = 4
    BaseRateAndLowEnergyCoreConfiguration = 3
    BaseRateCoreConfiguration = 2
    Camcorder = 13
    CapturingService = 8
    CarAudio = 8
    CardReaderPeripheral = 6
    CellularPhone = 1
    CommonIsdnAccessPhone = 5
    ComputerDevice = 1
    CordlessPhone = 2
    DataComplete = 0
    DataIncomplete = 1
    DataUnavailable = 2
    DesktopComputer = 1
    DigitizerTabletPeripheral = 5
    GamepadPeripheral = 2
    GamingDevice = 18
    HandheldClamShellComputer = 4
    HandheldComputer = 5
    HandsFreeDevice = 2
    Headphones = 6
    HealthBloodPressureMonitor = 1
    HealthDataDisplay = 7
    HealthDevice = 9
    HealthGlucoseMeter = 4
    HealthPulseOximeter = 5
    HealthStepCounter = 8
    HealthThermometer = 2
    HealthWeightScale = 3
    HiFiAudioDevice = 10
    ImageCamera = 8
    ImageDisplay = 4
    ImagePrinter = 32
    ImageScanner = 16
    ImagingDevice = 6
    InformationService = 128
    JoystickPeripheral = 1
    KeyboardPeripheral = 16
    KeyboardWithPointingDevicePeripheral = 48
    LANAccessDevice = 3
    LaptopComputer = 3
    Loudspeaker = 5
    LowEnergyCoreConfiguration = 1
    Microphone = 4
    MiscellaneousDevice = 0
    NetworkFullService = 0
    NetworkingService = 2
    NetworkLoadFactorFive = 40
    NetworkLoadFactorFour = 32
    NetworkLoadFactorOne = 8
    NetworkLoadFactorSix = 48
    NetworkLoadFactorThree = 24
    NetworkLoadFactorTwo = 16
    NetworkNoService = 56
    NoService = 0
    ObjectTransferService = 16
    PeripheralDevice = 5
    PhoneDevice = 2
    PointingDevicePeripheral = 32
    PortableAudioDevice = 7
    PositioningService = 1
    RemoteControlPeripheral = 3
    RenderingService = 4
    SensingDevicePeripheral = 4
    ServerComputer = 2
    SetTopBox = 9
    SmartPhone = 3
    TelephonyService = 64
    ToyController = 4
    ToyDevice = 8
    ToyDoll = 3
    ToyGame = 5
    ToyRobot = 1
    ToyVehicle = 2
    UncategorizedAudioVideoDevice = 0
    UncategorizedComputer = 0
    UncategorizedDevice = 31
    UncategorizedHealthDevice = 0
    UncategorizedImagingDevice = 0
    UncategorizedMiscellaneous = 0
    UncategorizedPeripheral = 0
    UncategorizedPhone = 0
    UncategorizedToy = 0
    UncategorizedWearableDevice = 0
    UnknownCoreConfiguration = 0
    Vcr = 11
    VideoCamera = 12
    VideoConferencing = 16
    VideoDisplayAndLoudspeaker = 15
    VideoMonitor = 14
    WearableComputer = 6
    WearableDevice = 7
    WearableGlasses = 5
    WearableHeadsetDevice = 1
    WearableHelmet = 4
    WearableJacket = 3
    WearablePager = 2
    WearableWristWatch = 1
    WiredModemOrVoiceGatewayPhone = 4
    __hash__ = None


class QBluetoothHostInfo(): # skipped bases: <class 'sip.wrapper'>
    """
    QBluetoothHostInfo()
    QBluetoothHostInfo(QBluetoothHostInfo)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setAddress(self, QBluetoothAddress): # real signature unknown; restored from __doc__
        """ setAddress(self, QBluetoothAddress) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ setName(self, str) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QBluetoothHostInfo=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QBluetoothLocalDevice(__PyQt5_QtCore.QObject):
    """
    QBluetoothLocalDevice(parent: QObject = None)
    QBluetoothLocalDevice(QBluetoothAddress, parent: QObject = None)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def allDevices(self): # real signature unknown; restored from __doc__
        """ allDevices() -> object """
        return object()

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectedDevices(self): # real signature unknown; restored from __doc__
        """ connectedDevices(self) -> object """
        return object()

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deviceConnected(self, QBluetoothAddress): # real signature unknown; restored from __doc__
        """ deviceConnected(self, QBluetoothAddress) [signal] """
        pass

    def deviceDisconnected(self, QBluetoothAddress): # real signature unknown; restored from __doc__
        """ deviceDisconnected(self, QBluetoothAddress) [signal] """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QBluetoothLocalDevice_Error): # real signature unknown; restored from __doc__
        """ error(self, QBluetoothLocalDevice.Error) [signal] """
        pass

    def hostMode(self): # real signature unknown; restored from __doc__
        """ hostMode(self) -> QBluetoothLocalDevice.HostMode """
        pass

    def hostModeStateChanged(self, QBluetoothLocalDevice_HostMode): # real signature unknown; restored from __doc__
        """ hostModeStateChanged(self, QBluetoothLocalDevice.HostMode) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def pairingConfirmation(self, bool): # real signature unknown; restored from __doc__
        """ pairingConfirmation(self, bool) """
        pass

    def pairingDisplayConfirmation(self, QBluetoothAddress, p_str): # real signature unknown; restored from __doc__
        """ pairingDisplayConfirmation(self, QBluetoothAddress, str) [signal] """
        pass

    def pairingDisplayPinCode(self, QBluetoothAddress, p_str): # real signature unknown; restored from __doc__
        """ pairingDisplayPinCode(self, QBluetoothAddress, str) [signal] """
        pass

    def pairingFinished(self, QBluetoothAddress, QBluetoothLocalDevice_Pairing): # real signature unknown; restored from __doc__
        """ pairingFinished(self, QBluetoothAddress, QBluetoothLocalDevice.Pairing) [signal] """
        pass

    def pairingStatus(self, QBluetoothAddress): # real signature unknown; restored from __doc__
        """ pairingStatus(self, QBluetoothAddress) -> QBluetoothLocalDevice.Pairing """
        pass

    def powerOn(self): # real signature unknown; restored from __doc__
        """ powerOn(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def requestPairing(self, QBluetoothAddress, QBluetoothLocalDevice_Pairing): # real signature unknown; restored from __doc__
        """ requestPairing(self, QBluetoothAddress, QBluetoothLocalDevice.Pairing) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setHostMode(self, QBluetoothLocalDevice_HostMode): # real signature unknown; restored from __doc__
        """ setHostMode(self, QBluetoothLocalDevice.HostMode) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AuthorizedPaired = 2
    HostConnectable = 1
    HostDiscoverable = 2
    HostDiscoverableLimitedInquiry = 3
    HostPoweredOff = 0
    NoError = 0
    Paired = 1
    PairingError = 1
    UnknownError = 100
    Unpaired = 0


class QBluetoothServer(__PyQt5_QtCore.QObject):
    """ QBluetoothServer(QBluetoothServiceInfo.Protocol, parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QBluetoothServer_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QBluetoothServer.Error
        error(self, QBluetoothServer.Error) [signal]
        """
        pass

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ hasPendingConnections(self) -> bool """
        return False

    def isListening(self): # real signature unknown; restored from __doc__
        """ isListening(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def listen(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        listen(self, address: QBluetoothAddress = QBluetoothAddress(), port: int = 0) -> bool
        listen(self, QBluetoothUuid, serviceName: str = '') -> QBluetoothServiceInfo
        """
        return QBluetoothServiceInfo

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ maxPendingConnections(self) -> int """
        return 0

    def newConnection(self): # real signature unknown; restored from __doc__
        """ newConnection(self) [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ nextPendingConnection(self) -> QBluetoothSocket """
        return QBluetoothSocket

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def securityFlags(self): # real signature unknown; restored from __doc__
        """ securityFlags(self) -> QBluetooth.SecurityFlags """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serverAddress(self): # real signature unknown; restored from __doc__
        """ serverAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def serverPort(self): # real signature unknown; restored from __doc__
        """ serverPort(self) -> int """
        return 0

    def serverType(self): # real signature unknown; restored from __doc__
        """ serverType(self) -> QBluetoothServiceInfo.Protocol """
        pass

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxPendingConnections(self, int) """
        pass

    def setSecurityFlags(self, Union, QBluetooth_SecurityFlags=None, QBluetooth_Security=None): # real signature unknown; restored from __doc__
        """ setSecurityFlags(self, Union[QBluetooth.SecurityFlags, QBluetooth.Security]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QBluetoothServiceInfo_Protocol, parent=None): # real signature unknown; restored from __doc__
        pass

    InputOutputError = 3
    NoError = 0
    PoweredOffError = 2
    ServiceAlreadyRegisteredError = 4
    UnknownError = 1
    UnsupportedProtocolError = 5


class QBluetoothServiceDiscoveryAgent(__PyQt5_QtCore.QObject):
    """
    QBluetoothServiceDiscoveryAgent(parent: QObject = None)
    QBluetoothServiceDiscoveryAgent(QBluetoothAddress, parent: QObject = None)
    """
    def canceled(self): # real signature unknown; restored from __doc__
        """ canceled(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def discoveredServices(self): # real signature unknown; restored from __doc__
        """ discoveredServices(self) -> object """
        return object()

    def error(self, QBluetoothServiceDiscoveryAgent_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QBluetoothServiceDiscoveryAgent.Error
        error(self, QBluetoothServiceDiscoveryAgent.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remoteAddress(self): # real signature unknown; restored from __doc__
        """ remoteAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceDiscovered(self, QBluetoothServiceInfo): # real signature unknown; restored from __doc__
        """ serviceDiscovered(self, QBluetoothServiceInfo) [signal] """
        pass

    def setRemoteAddress(self, QBluetoothAddress): # real signature unknown; restored from __doc__
        """ setRemoteAddress(self, QBluetoothAddress) -> bool """
        return False

    def setUuidFilter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setUuidFilter(self, Iterable[QBluetoothUuid])
        setUuidFilter(self, QBluetoothUuid)
        """
        pass

    def start(self, mode=None): # real signature unknown; restored from __doc__
        """ start(self, mode: QBluetoothServiceDiscoveryAgent.DiscoveryMode = QBluetoothServiceDiscoveryAgent.MinimalDiscovery) """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uuidFilter(self): # real signature unknown; restored from __doc__
        """ uuidFilter(self) -> List[QBluetoothUuid] """
        return []

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    FullDiscovery = 1
    InputOutputError = 1
    InvalidBluetoothAdapterError = 3
    MinimalDiscovery = 0
    NoError = 0
    PoweredOffError = 2
    UnknownError = 100


class QBluetoothServiceInfo(): # skipped bases: <class 'sip.wrapper'>
    """
    QBluetoothServiceInfo()
    QBluetoothServiceInfo(QBluetoothServiceInfo)
    """
    def attribute(self, p_int): # real signature unknown; restored from __doc__
        """ attribute(self, int) -> Any """
        pass

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> List[int] """
        return []

    def contains(self, p_int): # real signature unknown; restored from __doc__
        """ contains(self, int) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> QBluetoothDeviceInfo """
        return QBluetoothDeviceInfo

    def isComplete(self): # real signature unknown; restored from __doc__
        """ isComplete(self) -> bool """
        return False

    def isRegistered(self): # real signature unknown; restored from __doc__
        """ isRegistered(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def protocolDescriptor(self, QBluetoothUuid_ProtocolUuid): # real signature unknown; restored from __doc__
        """ protocolDescriptor(self, QBluetoothUuid.ProtocolUuid) -> List[Any] """
        return []

    def protocolServiceMultiplexer(self): # real signature unknown; restored from __doc__
        """ protocolServiceMultiplexer(self) -> int """
        return 0

    def registerService(self, localAdapter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ registerService(self, localAdapter: QBluetoothAddress = QBluetoothAddress()) -> bool """
        pass

    def removeAttribute(self, p_int): # real signature unknown; restored from __doc__
        """ removeAttribute(self, int) """
        pass

    def serverChannel(self): # real signature unknown; restored from __doc__
        """ serverChannel(self) -> int """
        return 0

    def serviceAvailability(self): # real signature unknown; restored from __doc__
        """ serviceAvailability(self) -> int """
        return 0

    def serviceClassUuids(self): # real signature unknown; restored from __doc__
        """ serviceClassUuids(self) -> List[QBluetoothUuid] """
        return []

    def serviceDescription(self): # real signature unknown; restored from __doc__
        """ serviceDescription(self) -> str """
        return ""

    def serviceName(self): # real signature unknown; restored from __doc__
        """ serviceName(self) -> str """
        return ""

    def serviceProvider(self): # real signature unknown; restored from __doc__
        """ serviceProvider(self) -> str """
        return ""

    def serviceUuid(self): # real signature unknown; restored from __doc__
        """ serviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def setAttribute(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttribute(self, int, QBluetoothUuid)
        setAttribute(self, int, Iterable[Any])
        setAttribute(self, int, Any)
        """
        pass

    def setDevice(self, QBluetoothDeviceInfo): # real signature unknown; restored from __doc__
        """ setDevice(self, QBluetoothDeviceInfo) """
        pass

    def setServiceAvailability(self, p_int): # real signature unknown; restored from __doc__
        """ setServiceAvailability(self, int) """
        pass

    def setServiceDescription(self, p_str): # real signature unknown; restored from __doc__
        """ setServiceDescription(self, str) """
        pass

    def setServiceName(self, p_str): # real signature unknown; restored from __doc__
        """ setServiceName(self, str) """
        pass

    def setServiceProvider(self, p_str): # real signature unknown; restored from __doc__
        """ setServiceProvider(self, str) """
        pass

    def setServiceUuid(self, QBluetoothUuid): # real signature unknown; restored from __doc__
        """ setServiceUuid(self, QBluetoothUuid) """
        pass

    def socketProtocol(self): # real signature unknown; restored from __doc__
        """ socketProtocol(self) -> QBluetoothServiceInfo.Protocol """
        pass

    def unregisterService(self): # real signature unknown; restored from __doc__
        """ unregisterService(self) -> bool """
        return False

    def __init__(self, QBluetoothServiceInfo=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AdditionalProtocolDescriptorList = 13
    BluetoothProfileDescriptorList = 9
    BrowseGroupList = 5
    ClientExecutableUrl = 11
    DocumentationUrl = 10
    IconUrl = 12
    L2capProtocol = 1
    LanguageBaseAttributeIdList = 6
    PrimaryLanguageBase = 256
    ProtocolDescriptorList = 4
    RfcommProtocol = 2
    ServiceAvailability = 8
    ServiceClassIds = 1
    ServiceDescription = 257
    ServiceId = 3
    ServiceInfoTimeToLive = 7
    ServiceName = 256
    ServiceProvider = 258
    ServiceRecordHandle = 0
    ServiceRecordState = 2
    UnknownProtocol = 0


class QBluetoothSocket(__PyQt5_QtCore.QIODevice):
    """
    QBluetoothSocket(QBluetoothServiceInfo.Protocol, parent: QObject = None)
    QBluetoothSocket(parent: QObject = None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def connected(self): # real signature unknown; restored from __doc__
        """ connected(self) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToService(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectToService(self, QBluetoothServiceInfo, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        connectToService(self, QBluetoothAddress, QBluetoothUuid, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        connectToService(self, QBluetoothAddress, int, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)
        """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self): # real signature unknown; restored from __doc__
        """ disconnected(self) [signal] """
        pass

    def disconnectFromService(self): # real signature unknown; restored from __doc__
        """ disconnectFromService(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doDeviceDiscovery(self, QBluetoothServiceInfo, Union, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None): # real signature unknown; restored from __doc__
        """ doDeviceDiscovery(self, QBluetoothServiceInfo, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) """
        pass

    def error(self, QBluetoothSocket_SocketError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QBluetoothSocket.SocketError
        error(self, QBluetoothSocket.SocketError) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def localPort(self): # real signature unknown; restored from __doc__
        """ localPort(self) -> int """
        return 0

    def peerAddress(self): # real signature unknown; restored from __doc__
        """ peerAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def peerName(self): # real signature unknown; restored from __doc__
        """ peerName(self) -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ peerPort(self) -> int """
        return 0

    def preferredSecurityFlags(self): # real signature unknown; restored from __doc__
        """ preferredSecurityFlags(self) -> QBluetooth.SecurityFlags """
        pass

    def readData(self, p_int): # real signature unknown; restored from __doc__
        """ readData(self, int) -> bytes """
        return b""

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPreferredSecurityFlags(self, Union, QBluetooth_SecurityFlags=None, QBluetooth_Security=None): # real signature unknown; restored from __doc__
        """ setPreferredSecurityFlags(self, Union[QBluetooth.SecurityFlags, QBluetooth.Security]) """
        pass

    def setSocketDescriptor(self, p_int, QBluetoothServiceInfo_Protocol, state=None, mode, QIODevice_OpenMode=None, QIODevice_OpenModeFlag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setSocketDescriptor(self, int, QBluetoothServiceInfo.Protocol, state: QBluetoothSocket.SocketState = QBluetoothSocket.ConnectedState, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool """
        pass

    def setSocketError(self, QBluetoothSocket_SocketError): # real signature unknown; restored from __doc__
        """ setSocketError(self, QBluetoothSocket.SocketError) """
        pass

    def setSocketState(self, QBluetoothSocket_SocketState): # real signature unknown; restored from __doc__
        """ setSocketState(self, QBluetoothSocket.SocketState) """
        pass

    def socketDescriptor(self): # real signature unknown; restored from __doc__
        """ socketDescriptor(self) -> int """
        return 0

    def socketType(self): # real signature unknown; restored from __doc__
        """ socketType(self) -> QBluetoothServiceInfo.Protocol """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QBluetoothSocket.SocketState """
        pass

    def stateChanged(self, QBluetoothSocket_SocketState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QBluetoothSocket.SocketState) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, bytes): # real signature unknown; restored from __doc__
        """ writeData(self, bytes) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    BoundState = 4
    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    HostNotFoundError = 2
    ListeningState = 5
    NetworkError = 7
    NoSocketError = -2
    OperationError = 19
    ServiceLookupState = 1
    ServiceNotFoundError = 9
    UnconnectedState = 0
    UnknownSocketError = -1
    UnsupportedProtocolError = 8


class QBluetoothTransferManager(__PyQt5_QtCore.QObject):
    """ QBluetoothTransferManager(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, QBluetoothTransferReply): # real signature unknown; restored from __doc__
        """ finished(self, QBluetoothTransferReply) [signal] """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, QBluetoothTransferRequest, QIODevice): # real signature unknown; restored from __doc__
        """ put(self, QBluetoothTransferRequest, QIODevice) -> QBluetoothTransferReply """
        return QBluetoothTransferReply

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


class QBluetoothTransferReply(__PyQt5_QtCore.QObject):
    """ QBluetoothTransferReply(parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QBluetoothTransferReply_TransferError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QBluetoothTransferReply.TransferError
        error(self, QBluetoothTransferReply.TransferError) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, QBluetoothTransferReply): # real signature unknown; restored from __doc__
        """ finished(self, QBluetoothTransferReply) [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def manager(self): # real signature unknown; restored from __doc__
        """ manager(self) -> QBluetoothTransferManager """
        return QBluetoothTransferManager

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self): # real signature unknown; restored from __doc__
        """ request(self) -> QBluetoothTransferRequest """
        return QBluetoothTransferRequest

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setManager(self, QBluetoothTransferManager): # real signature unknown; restored from __doc__
        """ setManager(self, QBluetoothTransferManager) """
        pass

    def setRequest(self, QBluetoothTransferRequest): # real signature unknown; restored from __doc__
        """ setRequest(self, QBluetoothTransferRequest) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def transferProgress(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ transferProgress(self, int, int) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    FileNotFoundError = 2
    HostNotFoundError = 3
    IODeviceNotReadableError = 5
    NoError = 0
    ResourceBusyError = 6
    SessionError = 7
    UnknownError = 1
    UserCanceledTransferError = 4


class QBluetoothTransferRequest(): # skipped bases: <class 'sip.wrapper'>
    """
    QBluetoothTransferRequest(address: QBluetoothAddress = QBluetoothAddress())
    QBluetoothTransferRequest(QBluetoothTransferRequest)
    """
    def address(self): # real signature unknown; restored from __doc__
        """ address(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def attribute(self, QBluetoothTransferRequest_Attribute, defaultValue=None): # real signature unknown; restored from __doc__
        """ attribute(self, QBluetoothTransferRequest.Attribute, defaultValue: Any = None) -> Any """
        pass

    def setAttribute(self, QBluetoothTransferRequest_Attribute, Any): # real signature unknown; restored from __doc__
        """ setAttribute(self, QBluetoothTransferRequest.Attribute, Any) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DescriptionAttribute = 0
    LengthAttribute = 3
    NameAttribute = 4
    TimeAttribute = 1
    TypeAttribute = 2
    __hash__ = None


class QBluetoothUuid(__PyQt5_QtCore.QUuid):
    """
    QBluetoothUuid()
    QBluetoothUuid(int)
    QBluetoothUuid(Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int)
    QBluetoothUuid(str)
    QBluetoothUuid(QBluetoothUuid)
    QBluetoothUuid(QUuid)
    """
    def characteristicToString(self, QBluetoothUuid_CharacteristicType): # real signature unknown; restored from __doc__
        """ characteristicToString(QBluetoothUuid.CharacteristicType) -> str """
        return ""

    def descriptorToString(self, QBluetoothUuid_DescriptorType): # real signature unknown; restored from __doc__
        """ descriptorToString(QBluetoothUuid.DescriptorType) -> str """
        return ""

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> int """
        return 0

    def protocolToString(self, QBluetoothUuid_ProtocolUuid): # real signature unknown; restored from __doc__
        """ protocolToString(QBluetoothUuid.ProtocolUuid) -> str """
        return ""

    def serviceClassToString(self, QBluetoothUuid_ServiceClassUuid): # real signature unknown; restored from __doc__
        """ serviceClassToString(QBluetoothUuid.ServiceClassUuid) -> str """
        return ""

    def toUInt128(self): # real signature unknown; restored from __doc__
        """ toUInt128(self) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int """
        pass

    def toUInt16(self): # real signature unknown; restored from __doc__
        """ toUInt16(self) -> Tuple[int, bool] """
        pass

    def toUInt32(self): # real signature unknown; restored from __doc__
        """ toUInt32(self) -> Tuple[int, bool] """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    AdvancedAudioDistribution = 4365
    AerobicHeartRateLowerLimit = 10878
    AerobicHeartRateUpperLimit = 10884
    AerobicThreshold = 10879
    Age = 10880
    AlertCategoryID = 10819
    AlertCategoryIDBitMask = 10818
    AlertLevel = 10758
    AlertNotificationControlPoint = 10820
    AlertNotificationService = 6161
    AlertStatus = 10815
    AnaerobicHeartRateLowerLimit = 10881
    AnaerobicHeartRateUpperLimit = 10882
    AnaerobicThreshold = 10883
    ApparentWindDirection = 10867
    ApparentWindSpeed = 10866
    Appearance = 10753
    Att = 7
    AudioSink = 4363
    AudioSource = 4362
    Avctp = 23
    Avdtp = 25
    AV_RemoteControl = 4366
    AV_RemoteControlController = 4367
    AV_RemoteControlTarget = 4364
    BarometricPressureTrend = 10915
    BasicImage = 4378
    BasicPrinting = 4386
    BatteryLevel = 10777
    BatteryService = 6159
    BloodPressure = 6160
    BloodPressureFeature = 10825
    BloodPressureMeasurement = 10805
    Bnep = 15
    BodyComposition = 6171
    BodyCompositionFeature = 10907
    BodyCompositionMeasurement = 10908
    BodySensorLocation = 10808
    BondManagement = 6174
    BootKeyboardInputReport = 10786
    BootKeyboardOutputReport = 10802
    BootMouseInputReport = 10803
    BrowseGroupDescriptor = 4097
    CharacteristicAggregateFormat = 10501
    CharacteristicExtendedProperties = 10496
    CharacteristicPresentationFormat = 10500
    CharacteristicUserDescription = 10497
    ClientCharacteristicConfiguration = 10498
    Cmtp = 27
    ContinuousGlucoseMonitoring = 6175
    CSCFeature = 10844
    CSCMeasurement = 10843
    CurrentTime = 10795
    CurrentTimeService = 6149
    CyclingPower = 6168
    CyclingPowerControlPoint = 10854
    CyclingPowerFeature = 10853
    CyclingPowerMeasurement = 10851
    CyclingPowerVector = 10852
    CyclingSpeedAndCadence = 6166
    DatabaseChangeIncrement = 10905
    DateOfBirth = 10885
    DateOfThresholdAssessment = 10886
    DateTime = 10760
    DayDateTime = 10762
    DayOfWeek = 10761
    DescriptorValueChanged = 10877
    DeviceInformation = 6154
    DeviceName = 10752
    DewPoint = 10875
    DialupNetworking = 4355
    DirectPrinting = 4376
    DirectPrintingReferenceObjectsService = 4384
    Display3D = 4407
    DSTOffset = 10765
    Elevation = 10860
    EmailAddress = 10887
    EnvironmentalSensing = 6170
    EnvironmentalSensingConfiguration = 10507
    EnvironmentalSensingMeasurement = 10508
    EnvironmentalSensingTriggerSetting = 10509
    ExactTime256 = 10764
    ExternalReportReference = 10503
    FatBurnHeartRateLowerLimit = 10888
    FatBurnHeartRateUpperLimit = 10889
    FirmwareRevisionString = 10790
    FirstName = 10890
    FiveZoneHeartRateLimits = 10891
    Ftp = 10
    Gender = 10892
    GenericAccess = 6144
    GenericAttribute = 6145
    GenericAudio = 4611
    GenericFileTransfer = 4610
    GenericNetworking = 4609
    GenericTelephony = 4612
    Glasses3D = 4408
    Glucose = 6152
    GlucoseFeature = 10833
    GlucoseMeasurement = 10776
    GlucoseMeasurementContext = 10804
    GN = 4375
    GNSS = 4405
    GNSSServer = 4406
    GustFactor = 10868
    Handsfree = 4382
    HandsfreeAudioGateway = 4383
    HardcopyCableReplacement = 4389
    HardcopyControlChannel = 18
    HardcopyDataChannel = 20
    HardcopyNotification = 22
    HardwareRevisionString = 10791
    HCRPrint = 4390
    HCRScan = 4391
    HDP = 5120
    HDPSink = 5122
    HDPSource = 5121
    Headset = 4360
    HeadsetAG = 4370
    HeadsetHS = 4401
    HealthThermometer = 6153
    HeartRate = 6157
    HeartRateControlPoint = 10809
    HeartRateMax = 10893
    HeartRateMeasurement = 10807
    HeatIndex = 10874
    Height = 10894
    HIDControlPoint = 10828
    HIDInformation = 10826
    Hidp = 17
    HipCircumference = 10895
    Http = 12
    HumanInterfaceDevice = 6162
    HumanInterfaceDeviceService = 4388
    Humidity = 10863
    IEEE1107320601RegulatoryCertificationDataList = 10794
    ImagingAutomaticArchive = 4380
    ImagingReferenceObjects = 4381
    ImagingResponder = 4379
    ImmediateAlert = 6146
    IntermediateCuffPressure = 10806
    IntermediateTemperature = 10782
    Ip = 9
    IrMCSync = 4356
    IrMCSyncCommand = 4359
    Irradiance = 10871
    L2cap = 256
    LANAccessUsingPPP = 4354
    Language = 10914
    LastName = 10896
    LinkLoss = 6147
    LNControlPoint = 10859
    LNFeature = 10858
    LocalTimeInformation = 10767
    LocationAndNavigation = 6169
    LocationAndSpeed = 10855
    MagneticDeclination = 10796
    MagneticFluxDensity2D = 10912
    MagneticFluxDensity3D = 10913
    ManufacturerNameString = 10793
    MaximumRecommendedHeartRate = 10897
    McapControlChannel = 30
    McapDataChannel = 31
    MeasurementInterval = 10785
    MessageAccessProfile = 4404
    MessageAccessServer = 4402
    MessageNotificationServer = 4403
    ModelNumberString = 10788
    MPSProfile = 4410
    MPSService = 4411
    NAP = 4374
    Navigation = 10856
    NewAlert = 10822
    NextDSTChangeService = 6151
    Obex = 8
    OBEXFileTransfer = 4358
    ObexObjectPush = 4357
    PANU = 4373
    PeripheralPreferredConnectionParameters = 10756
    PeripheralPrivacyFlag = 10754
    PhoneAlertStatusService = 6158
    PhonebookAccess = 4400
    PhonebookAccessPCE = 4398
    PhonebookAccessPSE = 4399
    PnPID = 10832
    PnPInformation = 4608
    PollenConcentration = 10869
    PositionQuality = 10857
    Pressure = 10861
    PrintingStatus = 4387
    ProtocolMode = 10830
    PublicBrowseGroup = 4098
    Rainfall = 10872
    ReconnectionAddress = 10755
    RecordAccessControlPoint = 10834
    ReferencePrinting = 4377
    ReferenceTimeInformation = 10772
    ReferenceTimeUpdateService = 6150
    ReflectedUI = 4385
    Report = 10829
    ReportMap = 10827
    ReportReference = 10504
    RestingHeartRate = 10898
    Rfcomm = 3
    RingerControlPoint = 10816
    RingerSetting = 10817
    RSCFeature = 10836
    RSCMeasurement = 10835
    RunningSpeedAndCadence = 6164
    ScanIntervalWindow = 10831
    ScanParameters = 6163
    ScanRefresh = 10801
    SCControlPoint = 10837
    Sdp = 1
    SensorLocation = 10845
    SerialNumberString = 10789
    SerialPort = 4353
    ServerCharacteristicConfiguration = 10499
    ServiceChanged = 10757
    ServiceDiscoveryServer = 4096
    SIMAccess = 4397
    SoftwareRevisionString = 10792
    SportTypeForAerobicAnaerobicThresholds = 10899
    SupportedNewAlertCategory = 10823
    SupportedUnreadAlertCategory = 10824
    Synchronization3D = 4409
    SystemID = 10787
    Tcp = 4
    TcsAt = 6
    TcsBin = 5
    Temperature = 10862
    TemperatureMeasurement = 10780
    TemperatureType = 10781
    ThreeZoneHeartRateLimits = 10900
    TimeAccuracy = 10770
    TimeSource = 10771
    TimeUpdateControlPoint = 10774
    TimeUpdateState = 10775
    TimeWithDST = 10769
    TimeZone = 10766
    TrueWindDirection = 10865
    TrueWindSpeed = 10864
    TwoZoneHeartRateLimits = 10901
    TxPower = 6148
    TxPowerLevel = 10759
    UdiCPlain = 29
    Udp = 2
    UnknownDescriptorType = 0
    UnreadAlertStatus = 10821
    Upnp = 16
    UserControlPoint = 10911
    UserData = 6172
    UserIndex = 10906
    UVIndex = 10870
    ValidRange = 10502
    VideoDistribution = 4869
    VideoSink = 4868
    VideoSource = 4867
    VO2Max = 10902
    WaistCircumference = 10903
    Weight = 10904
    WeightMeasurement = 10909
    WeightScale = 6173
    WeightScaleFeature = 10910
    WindChill = 10873
    Wsp = 14
    __hash__ = None


class QLowEnergyCharacteristic(): # skipped bases: <class 'sip.wrapper'>
    """
    QLowEnergyCharacteristic()
    QLowEnergyCharacteristic(QLowEnergyCharacteristic)
    """
    def descriptor(self, QBluetoothUuid): # real signature unknown; restored from __doc__
        """ descriptor(self, QBluetoothUuid) -> QLowEnergyDescriptor """
        return QLowEnergyDescriptor

    def descriptors(self): # real signature unknown; restored from __doc__
        """ descriptors(self) -> object """
        return object()

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def properties(self): # real signature unknown; restored from __doc__
        """ properties(self) -> QLowEnergyCharacteristic.PropertyTypes """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QLowEnergyCharacteristic=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Broadcasting = 1
    ExtendedProperty = 128
    Indicate = 32
    Notify = 16
    Read = 2
    Unknown = 0
    Write = 8
    WriteNoResponse = 4
    WriteSigned = 64
    __hash__ = None


class QLowEnergyController(__PyQt5_QtCore.QObject):
    """
    QLowEnergyController(QBluetoothDeviceInfo, parent: QObject = None)
    QLowEnergyController(QBluetoothAddress, parent: QObject = None)
    QLowEnergyController(QBluetoothAddress, QBluetoothAddress, parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connected(self): # real signature unknown; restored from __doc__
        """ connected(self) [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectToDevice(self): # real signature unknown; restored from __doc__
        """ connectToDevice(self) """
        pass

    def createServiceObject(self, QBluetoothUuid, parent=None): # real signature unknown; restored from __doc__
        """ createServiceObject(self, QBluetoothUuid, parent: QObject = None) -> QLowEnergyService """
        return QLowEnergyService

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self): # real signature unknown; restored from __doc__
        """ disconnected(self) [signal] """
        pass

    def disconnectFromDevice(self): # real signature unknown; restored from __doc__
        """ disconnectFromDevice(self) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def discoverServices(self): # real signature unknown; restored from __doc__
        """ discoverServices(self) """
        pass

    def discoveryFinished(self): # real signature unknown; restored from __doc__
        """ discoveryFinished(self) [signal] """
        pass

    def error(self, QLowEnergyController_Error=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QLowEnergyController.Error
        error(self, QLowEnergyController.Error) [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self): # real signature unknown; restored from __doc__
        """ localAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remoteAddress(self): # real signature unknown; restored from __doc__
        """ remoteAddress(self) -> QBluetoothAddress """
        return QBluetoothAddress

    def remoteAddressType(self): # real signature unknown; restored from __doc__
        """ remoteAddressType(self) -> QLowEnergyController.RemoteAddressType """
        pass

    def remoteName(self): # real signature unknown; restored from __doc__
        """ remoteName(self) -> str """
        return ""

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def serviceDiscovered(self, QBluetoothUuid): # real signature unknown; restored from __doc__
        """ serviceDiscovered(self, QBluetoothUuid) [signal] """
        pass

    def services(self): # real signature unknown; restored from __doc__
        """ services(self) -> List[QBluetoothUuid] """
        return []

    def setRemoteAddressType(self, QLowEnergyController_RemoteAddressType): # real signature unknown; restored from __doc__
        """ setRemoteAddressType(self, QLowEnergyController.RemoteAddressType) """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QLowEnergyController.ControllerState """
        pass

    def stateChanged(self, QLowEnergyController_ControllerState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QLowEnergyController.ControllerState) [signal] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ClosingState = 5
    ConnectedState = 2
    ConnectingState = 1
    ConnectionError = 5
    DiscoveredState = 4
    DiscoveringState = 3
    InvalidBluetoothAdapterError = 4
    NetworkError = 3
    NoError = 0
    PublicAddress = 0
    RandomAddress = 1
    UnconnectedState = 0
    UnknownError = 1
    UnknownRemoteDeviceError = 2


class QLowEnergyDescriptor(): # skipped bases: <class 'sip.wrapper'>
    """
    QLowEnergyDescriptor()
    QLowEnergyDescriptor(QLowEnergyDescriptor)
    """
    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QBluetoothUuid.DescriptorType """
        pass

    def uuid(self): # real signature unknown; restored from __doc__
        """ uuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QByteArray """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QLowEnergyDescriptor=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


class QLowEnergyService(__PyQt5_QtCore.QObject):
    # no doc
    def characteristic(self, QBluetoothUuid): # real signature unknown; restored from __doc__
        """ characteristic(self, QBluetoothUuid) -> QLowEnergyCharacteristic """
        return QLowEnergyCharacteristic

    def characteristicChanged(self, QLowEnergyCharacteristic, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ characteristicChanged(self, QLowEnergyCharacteristic, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def characteristicRead(self, QLowEnergyCharacteristic, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ characteristicRead(self, QLowEnergyCharacteristic, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def characteristics(self): # real signature unknown; restored from __doc__
        """ characteristics(self) -> object """
        return object()

    def characteristicWritten(self, QLowEnergyCharacteristic, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ characteristicWritten(self, QLowEnergyCharacteristic, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        contains(self, QLowEnergyCharacteristic) -> bool
        contains(self, QLowEnergyDescriptor) -> bool
        """
        return False

    def descriptorRead(self, QLowEnergyDescriptor, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ descriptorRead(self, QLowEnergyDescriptor, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def descriptorWritten(self, QLowEnergyDescriptor, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ descriptorWritten(self, QLowEnergyDescriptor, Union[QByteArray, bytes, bytearray]) [signal] """
        pass

    def discoverDetails(self): # real signature unknown; restored from __doc__
        """ discoverDetails(self) """
        pass

    def error(self, QLowEnergyService_ServiceError=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QLowEnergyService.ServiceError
        error(self, QLowEnergyService.ServiceError) [signal]
        """
        pass

    def includedServices(self): # real signature unknown; restored from __doc__
        """ includedServices(self) -> List[QBluetoothUuid] """
        return []

    def readCharacteristic(self, QLowEnergyCharacteristic): # real signature unknown; restored from __doc__
        """ readCharacteristic(self, QLowEnergyCharacteristic) """
        pass

    def readDescriptor(self, QLowEnergyDescriptor): # real signature unknown; restored from __doc__
        """ readDescriptor(self, QLowEnergyDescriptor) """
        pass

    def serviceName(self): # real signature unknown; restored from __doc__
        """ serviceName(self) -> str """
        return ""

    def serviceUuid(self): # real signature unknown; restored from __doc__
        """ serviceUuid(self) -> QBluetoothUuid """
        return QBluetoothUuid

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QLowEnergyService.ServiceState """
        pass

    def stateChanged(self, QLowEnergyService_ServiceState): # real signature unknown; restored from __doc__
        """ stateChanged(self, QLowEnergyService.ServiceState) [signal] """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QLowEnergyService.ServiceTypes """
        pass

    def writeCharacteristic(self, QLowEnergyCharacteristic, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ writeCharacteristic(self, QLowEnergyCharacteristic, Union[QByteArray, bytes, bytearray], mode: QLowEnergyService.WriteMode = QLowEnergyService.WriteWithResponse) """
        pass

    def writeDescriptor(self, QLowEnergyDescriptor, Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
        """ writeDescriptor(self, QLowEnergyDescriptor, Union[QByteArray, bytes, bytearray]) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CharacteristicReadError = 5
    CharacteristicWriteError = 2
    DescriptorReadError = 6
    DescriptorWriteError = 3
    DiscoveringServices = 2
    DiscoveryRequired = 1
    IncludedService = 2
    InvalidService = 0
    NoError = 0
    OperationError = 1
    PrimaryService = 1
    ServiceDiscovered = 3
    UnknownError = 4
    WriteWithoutResponse = 1
    WriteWithResponse = 0


# variables with complex values



