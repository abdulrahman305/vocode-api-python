# This file was auto-generated by Fern from our API Definition.

from .types import (
    ActionPage,
    ActionPageItemsItem,
    ActionPageItemsItem_ActionDtmf,
    ActionPageItemsItem_ActionEndConversation,
    ActionPageItemsItem_ActionTransferCall,
    ActionParamsRequest,
    ActionParamsRequest_ActionDtmf,
    ActionParamsRequest_ActionEndConversation,
    ActionParamsRequest_ActionTransferCall,
    ActionResponseModel,
    ActionResponseModel_ActionDtmf,
    ActionResponseModel_ActionEndConversation,
    ActionResponseModel_ActionTransferCall,
    ActionUpdateParamsRequest,
    ActionUpdateParamsRequest_ActionDtmf,
    ActionUpdateParamsRequest_ActionEndConversation,
    ActionUpdateParamsRequest_ActionTransferCall,
    Agent,
    AgentActionsItem,
    AgentActionsItem_ActionDtmf,
    AgentActionsItem_ActionEndConversation,
    AgentActionsItem_ActionTransferCall,
    AgentPage,
    AgentParamsActionsItem,
    AgentParamsActionsItemOne,
    AgentParamsActionsItemOne_ActionDtmf,
    AgentParamsActionsItemOne_ActionEndConversation,
    AgentParamsActionsItemOne_ActionTransferCall,
    AgentParamsVectorDatabase,
    AgentParamsVoice,
    AgentParamsVoiceOne,
    AgentParamsVoiceOne_VoiceAzure,
    AgentParamsVoiceOne_VoiceElevenLabs,
    AgentParamsVoiceOne_VoicePlayHt,
    AgentParamsVoiceOne_VoiceRime,
    AgentParamsWebhook,
    AgentUpdateParams,
    AgentUpdateParamsActions,
    AgentUpdateParamsActionsItem,
    AgentUpdateParamsActionsItemOne,
    AgentUpdateParamsActionsItemOne_ActionDtmf,
    AgentUpdateParamsActionsItemOne_ActionEndConversation,
    AgentUpdateParamsActionsItemOne_ActionTransferCall,
    AgentUpdateParamsContextEndpoint,
    AgentUpdateParamsInitialMessage,
    AgentUpdateParamsInterruptSensitivity,
    AgentUpdateParamsLanguage,
    AgentUpdateParamsPrompt,
    AgentUpdateParamsVectorDatabase,
    AgentUpdateParamsVoice,
    AgentUpdateParamsVoiceOne,
    AgentUpdateParamsVoiceOne_VoiceAzure,
    AgentUpdateParamsVoiceOne_VoiceElevenLabs,
    AgentUpdateParamsVoiceOne_VoicePlayHt,
    AgentUpdateParamsVoiceOne_VoiceRime,
    AgentUpdateParamsWebhook,
    AgentVoice,
    AgentVoice_VoiceAzure,
    AgentVoice_VoiceElevenLabs,
    AgentVoice_VoicePlayHt,
    AgentVoice_VoiceRime,
    AzureVoice,
    AzureVoiceParams,
    AzureVoiceUpdateParams,
    AzureVoiceUpdateParamsPitch,
    AzureVoiceUpdateParamsRate,
    AzureVoiceUpdateParamsVoiceName,
    Call,
    CallPage,
    CallStatus,
    CreateCallAgentParams,
    CreateCallAgentParamsActionsItem,
    CreateCallAgentParamsActionsItemOne,
    CreateCallAgentParamsActionsItemOne_ActionDtmf,
    CreateCallAgentParamsActionsItemOne_ActionEndConversation,
    CreateCallAgentParamsActionsItemOne_ActionTransferCall,
    CreateCallAgentParamsVectorDatabase,
    CreateCallAgentParamsVoice,
    CreateCallAgentParamsVoiceOne,
    CreateCallAgentParamsVoiceOne_VoiceAzure,
    CreateCallAgentParamsVoiceOne_VoiceElevenLabs,
    CreateCallAgentParamsVoiceOne_VoicePlayHt,
    CreateCallAgentParamsVoiceOne_VoiceRime,
    CreateCallAgentParamsWebhook,
    CreateCallRequestAgent,
    DtmfAction,
    DtmfActionParams,
    DtmfActionUpdateParams,
    DtmfActionUpdateParamsConfig,
    ElevenLabsVoice,
    ElevenLabsVoiceParams,
    ElevenLabsVoiceUpdateParams,
    ElevenLabsVoiceUpdateParamsApiKey,
    ElevenLabsVoiceUpdateParamsSimilarityBoost,
    ElevenLabsVoiceUpdateParamsStability,
    ElevenLabsVoiceUpdateParamsVoiceId,
    EmptyActionConfig,
    EndConversationAction,
    EndConversationActionParams,
    EndConversationActionUpdateParams,
    EndConversationActionUpdateParamsConfig,
    EventType,
    HttpMethod,
    HttpValidationError,
    InterruptSensitivity,
    Language,
    NormalizedAgent,
    NormalizedAgentVectorDatabase,
    NormalizedCall,
    NormalizedPhoneNumber,
    PhoneNumber,
    PhoneNumberPage,
    PineconeVectorDatabase,
    PineconeVectorDatabaseParams,
    PineconeVectorDatabaseUpdateParams,
    PineconeVectorDatabaseUpdateParamsApiEnvironment,
    PineconeVectorDatabaseUpdateParamsApiKey,
    PineconeVectorDatabaseUpdateParamsIndex,
    PlanType,
    PlayHtVoice,
    PlayHtVoiceParams,
    PlayHtVoiceUpdateParams,
    PlayHtVoiceUpdateParamsApiKey,
    PlayHtVoiceUpdateParamsApiUserId,
    PlayHtVoiceUpdateParamsVoiceId,
    RimeVoice,
    RimeVoiceParams,
    RimeVoiceUpdateParams,
    RimeVoiceUpdateParamsSpeaker,
    TransferCallAction,
    TransferCallActionParams,
    TransferCallActionUpdateParams,
    TransferCallActionUpdateParamsConfig,
    TransferCallConfig,
    Undefined,
    UpdateNumberRequestInboundAgent,
    UpdateNumberRequestLabel,
    Usage,
    ValidationError,
    ValidationErrorLocItem,
    VoicePage,
    VoicePageItemsItem,
    VoicePageItemsItem_VoiceAzure,
    VoicePageItemsItem_VoiceElevenLabs,
    VoicePageItemsItem_VoicePlayHt,
    VoicePageItemsItem_VoiceRime,
    VoiceParamsRequest,
    VoiceParamsRequest_VoiceAzure,
    VoiceParamsRequest_VoiceElevenLabs,
    VoiceParamsRequest_VoicePlayHt,
    VoiceParamsRequest_VoiceRime,
    VoiceResponseModel,
    VoiceResponseModel_VoiceAzure,
    VoiceResponseModel_VoiceElevenLabs,
    VoiceResponseModel_VoicePlayHt,
    VoiceResponseModel_VoiceRime,
    VoiceUpdateParamsRequest,
    VoiceUpdateParamsRequest_VoiceAzure,
    VoiceUpdateParamsRequest_VoiceElevenLabs,
    VoiceUpdateParamsRequest_VoicePlayHt,
    VoiceUpdateParamsRequest_VoiceRime,
    Webhook,
    WebhookPage,
    WebhookParams,
    WebhookUpdateParams,
    WebhookUpdateParamsMethod,
    WebhookUpdateParamsSubscriptions,
    WebhookUpdateParamsUrl,
)
from .errors import UnprocessableEntityError
from .resources import actions, agents, calls, numbers, usage, voices, webhooks

__all__ = [
    "ActionPage",
    "ActionPageItemsItem",
    "ActionPageItemsItem_ActionDtmf",
    "ActionPageItemsItem_ActionEndConversation",
    "ActionPageItemsItem_ActionTransferCall",
    "ActionParamsRequest",
    "ActionParamsRequest_ActionDtmf",
    "ActionParamsRequest_ActionEndConversation",
    "ActionParamsRequest_ActionTransferCall",
    "ActionResponseModel",
    "ActionResponseModel_ActionDtmf",
    "ActionResponseModel_ActionEndConversation",
    "ActionResponseModel_ActionTransferCall",
    "ActionUpdateParamsRequest",
    "ActionUpdateParamsRequest_ActionDtmf",
    "ActionUpdateParamsRequest_ActionEndConversation",
    "ActionUpdateParamsRequest_ActionTransferCall",
    "Agent",
    "AgentActionsItem",
    "AgentActionsItem_ActionDtmf",
    "AgentActionsItem_ActionEndConversation",
    "AgentActionsItem_ActionTransferCall",
    "AgentPage",
    "AgentParamsActionsItem",
    "AgentParamsActionsItemOne",
    "AgentParamsActionsItemOne_ActionDtmf",
    "AgentParamsActionsItemOne_ActionEndConversation",
    "AgentParamsActionsItemOne_ActionTransferCall",
    "AgentParamsVectorDatabase",
    "AgentParamsVoice",
    "AgentParamsVoiceOne",
    "AgentParamsVoiceOne_VoiceAzure",
    "AgentParamsVoiceOne_VoiceElevenLabs",
    "AgentParamsVoiceOne_VoicePlayHt",
    "AgentParamsVoiceOne_VoiceRime",
    "AgentParamsWebhook",
    "AgentUpdateParams",
    "AgentUpdateParamsActions",
    "AgentUpdateParamsActionsItem",
    "AgentUpdateParamsActionsItemOne",
    "AgentUpdateParamsActionsItemOne_ActionDtmf",
    "AgentUpdateParamsActionsItemOne_ActionEndConversation",
    "AgentUpdateParamsActionsItemOne_ActionTransferCall",
    "AgentUpdateParamsContextEndpoint",
    "AgentUpdateParamsInitialMessage",
    "AgentUpdateParamsInterruptSensitivity",
    "AgentUpdateParamsLanguage",
    "AgentUpdateParamsPrompt",
    "AgentUpdateParamsVectorDatabase",
    "AgentUpdateParamsVoice",
    "AgentUpdateParamsVoiceOne",
    "AgentUpdateParamsVoiceOne_VoiceAzure",
    "AgentUpdateParamsVoiceOne_VoiceElevenLabs",
    "AgentUpdateParamsVoiceOne_VoicePlayHt",
    "AgentUpdateParamsVoiceOne_VoiceRime",
    "AgentUpdateParamsWebhook",
    "AgentVoice",
    "AgentVoice_VoiceAzure",
    "AgentVoice_VoiceElevenLabs",
    "AgentVoice_VoicePlayHt",
    "AgentVoice_VoiceRime",
    "AzureVoice",
    "AzureVoiceParams",
    "AzureVoiceUpdateParams",
    "AzureVoiceUpdateParamsPitch",
    "AzureVoiceUpdateParamsRate",
    "AzureVoiceUpdateParamsVoiceName",
    "Call",
    "CallPage",
    "CallStatus",
    "CreateCallAgentParams",
    "CreateCallAgentParamsActionsItem",
    "CreateCallAgentParamsActionsItemOne",
    "CreateCallAgentParamsActionsItemOne_ActionDtmf",
    "CreateCallAgentParamsActionsItemOne_ActionEndConversation",
    "CreateCallAgentParamsActionsItemOne_ActionTransferCall",
    "CreateCallAgentParamsVectorDatabase",
    "CreateCallAgentParamsVoice",
    "CreateCallAgentParamsVoiceOne",
    "CreateCallAgentParamsVoiceOne_VoiceAzure",
    "CreateCallAgentParamsVoiceOne_VoiceElevenLabs",
    "CreateCallAgentParamsVoiceOne_VoicePlayHt",
    "CreateCallAgentParamsVoiceOne_VoiceRime",
    "CreateCallAgentParamsWebhook",
    "CreateCallRequestAgent",
    "DtmfAction",
    "DtmfActionParams",
    "DtmfActionUpdateParams",
    "DtmfActionUpdateParamsConfig",
    "ElevenLabsVoice",
    "ElevenLabsVoiceParams",
    "ElevenLabsVoiceUpdateParams",
    "ElevenLabsVoiceUpdateParamsApiKey",
    "ElevenLabsVoiceUpdateParamsSimilarityBoost",
    "ElevenLabsVoiceUpdateParamsStability",
    "ElevenLabsVoiceUpdateParamsVoiceId",
    "EmptyActionConfig",
    "EndConversationAction",
    "EndConversationActionParams",
    "EndConversationActionUpdateParams",
    "EndConversationActionUpdateParamsConfig",
    "EventType",
    "HttpMethod",
    "HttpValidationError",
    "InterruptSensitivity",
    "Language",
    "NormalizedAgent",
    "NormalizedAgentVectorDatabase",
    "NormalizedCall",
    "NormalizedPhoneNumber",
    "PhoneNumber",
    "PhoneNumberPage",
    "PineconeVectorDatabase",
    "PineconeVectorDatabaseParams",
    "PineconeVectorDatabaseUpdateParams",
    "PineconeVectorDatabaseUpdateParamsApiEnvironment",
    "PineconeVectorDatabaseUpdateParamsApiKey",
    "PineconeVectorDatabaseUpdateParamsIndex",
    "PlanType",
    "PlayHtVoice",
    "PlayHtVoiceParams",
    "PlayHtVoiceUpdateParams",
    "PlayHtVoiceUpdateParamsApiKey",
    "PlayHtVoiceUpdateParamsApiUserId",
    "PlayHtVoiceUpdateParamsVoiceId",
    "RimeVoice",
    "RimeVoiceParams",
    "RimeVoiceUpdateParams",
    "RimeVoiceUpdateParamsSpeaker",
    "TransferCallAction",
    "TransferCallActionParams",
    "TransferCallActionUpdateParams",
    "TransferCallActionUpdateParamsConfig",
    "TransferCallConfig",
    "Undefined",
    "UnprocessableEntityError",
    "UpdateNumberRequestInboundAgent",
    "UpdateNumberRequestLabel",
    "Usage",
    "ValidationError",
    "ValidationErrorLocItem",
    "VoicePage",
    "VoicePageItemsItem",
    "VoicePageItemsItem_VoiceAzure",
    "VoicePageItemsItem_VoiceElevenLabs",
    "VoicePageItemsItem_VoicePlayHt",
    "VoicePageItemsItem_VoiceRime",
    "VoiceParamsRequest",
    "VoiceParamsRequest_VoiceAzure",
    "VoiceParamsRequest_VoiceElevenLabs",
    "VoiceParamsRequest_VoicePlayHt",
    "VoiceParamsRequest_VoiceRime",
    "VoiceResponseModel",
    "VoiceResponseModel_VoiceAzure",
    "VoiceResponseModel_VoiceElevenLabs",
    "VoiceResponseModel_VoicePlayHt",
    "VoiceResponseModel_VoiceRime",
    "VoiceUpdateParamsRequest",
    "VoiceUpdateParamsRequest_VoiceAzure",
    "VoiceUpdateParamsRequest_VoiceElevenLabs",
    "VoiceUpdateParamsRequest_VoicePlayHt",
    "VoiceUpdateParamsRequest_VoiceRime",
    "Webhook",
    "WebhookPage",
    "WebhookParams",
    "WebhookUpdateParams",
    "WebhookUpdateParamsMethod",
    "WebhookUpdateParamsSubscriptions",
    "WebhookUpdateParamsUrl",
    "actions",
    "agents",
    "calls",
    "numbers",
    "usage",
    "voices",
    "webhooks",
]
