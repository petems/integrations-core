# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from types import MappingProxyType
from typing import Any, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class IncludeItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None
    uptime: Optional[bool] = None


class Hypervisor(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of hypervisors to be processed.\n')


class IncludeItem1(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    diagnostics: Optional[bool] = None
    flavors: Optional[bool] = None
    name: Optional[str] = None


class Server(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem1], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of servers to be processed.\n')


class ComputeItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    flavors: Optional[bool] = None
    hypervisors: Optional[Union[bool, Hypervisor]] = None
    limits: Optional[bool] = None
    quota_sets: Optional[bool] = None
    servers: Optional[Union[bool, Server]] = None
    services: Optional[bool] = None


class IdentityItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    domains: Optional[bool] = None
    groups: Optional[bool] = None
    limits: Optional[bool] = None
    projects: Optional[bool] = None
    regions: Optional[bool] = None
    services: Optional[bool] = None
    users: Optional[bool] = None


class IncludeItem2(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    name: Optional[str] = None


class Network(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, IncludeItem2], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of networks to be processed.\n')


class NetworkItem(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    agents: Optional[bool] = None
    networks: Optional[Union[bool, Network]] = None
    quotas: Optional[bool] = None


class Components(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    block_storage: Optional[Union[bool, MappingProxyType[str, Any]]] = Field(None, alias='block-storage')
    compute: Optional[Union[bool, ComputeItem]] = None
    identity: Optional[Union[bool, IdentityItem]] = None
    network: Optional[Union[bool, NetworkItem]] = None


class Projects(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
    )
    exclude: Optional[tuple[str, ...]] = None
    include: Optional[tuple[Union[str, MappingProxyType[str, Any]], ...]] = None
    interval: Optional[int] = None
    limit: Optional[int] = Field(None, description='Maximum number of clusters to be processed.\n')


class InstanceConfig(BaseModel):
    model_config = ConfigDict(
        validate_default=True,
        arbitrary_types_allowed=True,
        frozen=True,
    )
    blacklist_project_names: Optional[tuple[str, ...]] = None
    collect_hypervisor_load: Optional[bool] = None
    collect_hypervisor_metrics: Optional[bool] = None
    collect_network_metrics: Optional[bool] = None
    collect_project_metrics: Optional[bool] = None
    collect_server_diagnostic_metrics: Optional[bool] = None
    collect_server_flavor_metrics: Optional[bool] = None
    components: Optional[Components] = None
    domain_id: Optional[str] = None
    endpoint_interface: Optional[str] = None
    endpoint_region_id: Optional[str] = None
    exclude_network_ids: Optional[tuple[str, ...]] = None
    exclude_server_ids: Optional[tuple[str, ...]] = None
    ironic_microversion: Optional[str] = None
    keystone_server_url: Optional[str] = None
    name: Optional[str] = None
    nova_microversion: Optional[str] = None
    openstack_cloud_name: Optional[str] = None
    openstack_config_file_path: Optional[str] = None
    paginated_limit: Optional[int] = None
    password: Optional[str] = None
    projects: Optional[Projects] = None
    use_agent_proxy: Optional[bool] = None
    use_legacy_check_version: Optional[bool] = None
    use_shortname: Optional[bool] = None
    user: Optional[MappingProxyType[str, Any]] = None
    username: Optional[str] = None
    whitelist_project_names: Optional[tuple[str, ...]] = None

    @model_validator(mode='before')
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @field_validator('*', mode='before')
    def _validate(cls, value, info):
        field = cls.model_fields[info.field_name]
        field_name = field.alias or info.field_name
        if field_name in info.context['configured_fields']:
            value = getattr(validators, f'instance_{info.field_name}', identity)(value, field=field)
        else:
            value = getattr(defaults, f'instance_{info.field_name}', lambda: value)()

        return validation.utils.make_immutable(value)

    @model_validator(mode='after')
    def _final_validation(cls, model):
        return validation.core.check_model(getattr(validators, 'check_instance', identity)(model))
