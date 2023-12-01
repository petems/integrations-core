# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

import pytest

from datadog_checks.dev import get_docker_hostname, get_here

from .legacy.common import FLAVOR

HERE = get_here()
FIXTURE_DIR = os.path.join(HERE, 'fixtures')
DOCKER_DIR = os.path.join(HERE, 'docker')
ENVOY_VERSION = os.getenv('ENVOY_VERSION')

HOST = get_docker_hostname()
PORT = '8001'

URL = 'http://{}:{}'.format(HOST, PORT)
DEFAULT_INSTANCE = {'openmetrics_endpoint': '{}/stats/prometheus'.format(URL)}
requires_new_environment = pytest.mark.skipif(FLAVOR == 'api_v2', reason='Requires prometheus environment')

PROMETHEUS_METRICS = [
    "cluster.assignment_stale.count",
    "cluster.assignment_timeout_received.count",
    "cluster.bind_errors.count",
    "cluster.circuit_breakers.cx_open",
    "cluster.circuit_breakers.cx_pool_open",
    "cluster.circuit_breakers.rq_open",
    "cluster.circuit_breakers.rq_pending_open",
    "cluster.circuit_breakers.rq_retry_open",
    "cluster.default_total_match.count",
    "cluster.ext_authz.error.count",
    "cluster.ext_authz.failure_mode_allowed.count",
    "cluster.external.upstream_rq.count",
    "cluster.external.upstream_rq_completed.count",
    "cluster.external.upstream_rq_xx.count",
    "cluster.external.upstream_rq_time.bucket",
    "cluster.external.upstream_rq_time.count",
    "cluster.external.upstream_rq_time.sum",
    "cluster.http1.dropped_headers_with_underscores.count",
    "cluster.http1.metadata_not_supported_error.count",
    "cluster.http1.requests_rejected_with_underscores_in_headers.count",
    "cluster.http1.response_flood.count",
    "cluster.http2.dropped_headers_with_underscores.count",
    "cluster.http2.header_overflow.count",
    "cluster.http2.headers_cb_no_stream.count",
    "cluster.http2.inbound_empty_frames_flood.count",
    "cluster.http2.inbound_priority_frames_flood.count",
    "cluster.http2.inbound_window_update_frames_flood.count",
    "cluster.http2.keepalive_timeout.count",
    "cluster.http2.metadata_empty_frames.count",
    "cluster.http2.outbound_control_flood.count",
    "cluster.http2.outbound_flood.count",
    "cluster.http2.pending_send_bytes",
    "cluster.http2.requests_rejected_with_underscores_in_headers.count",
    "cluster.http2.rx_messaging_error.count",
    "cluster.http2.rx_reset.count",
    "cluster.http2.streams_active",
    "cluster.http2.trailers.count",
    "cluster.http2.tx_flush_timeout.count",
    "cluster.http2.tx_reset.count",
    "cluster.internal.upstream_rq.count",
    "cluster.internal.upstream_rq_completed.count",
    "cluster.internal.upstream_rq_xx.count",
    "cluster.lb_healthy_panic.count",
    "cluster.lb_local_cluster_not_ok.count",
    "cluster.lb_recalculate_zone_structures.count",
    "cluster.lb_subsets_active",
    "cluster.lb_subsets_created.count",
    "cluster.lb_subsets_fallback.count",
    "cluster.lb_subsets_fallback_panic.count",
    "cluster.lb_subsets_removed.count",
    "cluster.lb_subsets_selected.count",
    "cluster.lb_zone_cluster_too_small.count",
    "cluster.lb_zone_no_capacity_left.count",
    "cluster.lb_zone_number_differs.count",
    "cluster.lb_zone_routing_all_directly.count",
    "cluster.lb_zone_routing_cross_zone.count",
    "cluster.lb_zone_routing_sampled.count",
    "cluster.max_host_weight",
    "cluster.membership_change.count",
    "cluster.membership_degraded",
    "cluster.membership_excluded",
    "cluster.membership_healthy",
    "cluster.membership_total",
    "cluster.original_dst_host_invalid.count",
    "cluster.ratelimit.error.count",
    "cluster.ratelimit.failure_mode_allowed.count",
    "cluster.retry_or_shadow_abandoned.count",
    "cluster.update_attempt.count",
    "cluster.update_empty.count",
    "cluster.update_failure.count",
    "cluster.update_no_rebuild.count",
    "cluster.update_success.count",
    "cluster.upstream_cx_active",
    "cluster.upstream_cx_close_notify.count",
    "cluster.upstream_cx_connect_attempts_exceeded.count",
    "cluster.upstream_cx_connect_fail.count",
    "cluster.upstream_cx_connect_ms.bucket",
    "cluster.upstream_cx_connect_ms.count",
    "cluster.upstream_cx_connect_ms.sum",
    "cluster.upstream_cx_connect_timeout.count",
    "cluster.upstream_cx_destroy.count",
    "cluster.upstream_cx_destroy_local.count",
    "cluster.upstream_cx_destroy_local_with_active_rq.count",
    "cluster.upstream_cx_destroy_remote_with_active_rq.count",
    "cluster.upstream_cx_destroy_remote.count",
    "cluster.upstream_cx_destroy_with_active_rq.count",
    "cluster.upstream_cx_idle_timeout.count",
    "cluster.upstream_cx_length_ms.bucket",
    "cluster.upstream_cx_length_ms.count",
    "cluster.upstream_cx_length_ms.sum",
    "cluster.upstream_cx_max_requests.count",
    "cluster.upstream_cx_none_healthy.count",
    "cluster.upstream_cx_overflow.count",
    "cluster.upstream_cx_pool_overflow.count",
    "cluster.upstream_cx_protocol_error.count",
    "cluster.upstream_cx_rx_bytes_buffered",
    "cluster.upstream_cx_tx_bytes_buffered",
    "cluster.upstream_rq.count",
    "cluster.upstream_rq_active",
    "cluster.upstream_rq_cancelled.count",
    "cluster.upstream_rq_completed.count",
    "cluster.upstream_rq_maintenance_mode.count",
    "cluster.upstream_rq_max_duration_reached.count",
    "cluster.upstream_rq_pending_active",
    "cluster.upstream_rq_pending_failure_eject.count",
    "cluster.upstream_rq_pending_overflow.count",
    "cluster.upstream_rq_per_try_timeout.count",
    "cluster.upstream_rq_retry.count",
    "cluster.upstream_rq_retry_backoff_exponential.count",
    "cluster.upstream_rq_retry_backoff_ratelimited.count",
    "cluster.upstream_rq_retry_limit_exceeded.count",
    "cluster.upstream_rq_retry_overflow.count",
    "cluster.upstream_rq_retry_success.count",
    "cluster.upstream_rq_rx_reset.count",
    "cluster.upstream_rq_timeout.count",
    "cluster.upstream_rq_tx_reset.count",
    "cluster.upstream_rq_xx.count",
    "cluster.version",
    "cluster_manager.active_clusters",
    "cluster_manager.cds.control_plane.connected_state",
    "cluster_manager.cds.control_plane.pending_requests",
    "cluster_manager.cds.control_plane.rate_limit_enforced.count",
    "cluster_manager.cds.init_fetch_timeout.count",
    "cluster_manager.cds.update_attempt.count",
    "cluster_manager.cds.update_duration.bucket",
    "cluster_manager.cds.update_duration.count",
    "cluster_manager.cds.update_duration.sum",
    "cluster_manager.cds.update_failure.count",
    "cluster_manager.cds.update_rejected.count",
    "cluster_manager.cds.update_success.count",
    "cluster_manager.cds.update_time",
    "cluster_manager.cds.version",
    "cluster_manager.cluster_added.count",
    "cluster_manager.cluster_modified.count",
    "cluster_manager.cluster_removed.count",
    "cluster_manager.cluster_updated.count",
    "cluster_manager.custer_updated_via_merge.count",
    "cluster_manager.update_merge_cancelled.count",
    "cluster_manager.update_out_of_merge_window.count",
    "cluster_manager.warming_clusters",
    "filesystem.flushed_by_timer.count",
    "filesystem.reopen_failed.count",
    "filesystem.write_buffered.count",
    "filesystem.write_completed.count",
    "filesystem.write_failed.count",
    "filesystem.write_total_buffered",
    "http.downstream_cx_active",
    "http.downstream_cx_delayed_close_timeout.count",
    "http.downstream_cx_destroy.count",
    "http.downstream_cx_destroy_active_rq.count",
    "http.downstream_cx_destroy_local.count",
    "http.downstream_cx_destroy_local_active_rq.count",
    "http.downstream_cx_destroy_remote.count",
    "http.downstream_cx_destroy_remote_active_rq.count",
    "http.downstream_cx_drain_close.count",
    "http.downstream_cx_http1_active",
    "http.downstream_cx_http2_active",
    "http.downstream_cx_http3_active",
    "http.downstream_cx_idle_timeout.count",
    "http.downstream_cx_max_duration_reached.count",
    "http.downstream_cx_overload_disable_keepalive.count",
    "http.downstream_cx_protocol_error.count",
    "http.downstream_cx_rx_bytes_buffered",
    "http.downstream_cx_ssl_active",
    "http.downstream_cx_tx_bytes_buffered",
    "http.downstream_cx_upgrades_active",
    "http.downstream_rq_active",
    "http.downstream_rq_completed.count",
    "http.downstream_rq_failed_path_normalization.count",
    "http.downstream_rq_header_timeout.count",
    "http.downstream_rq_idle_timeout.count",
    "http.downstream_rq_max_duration_reached.count",
    "http.downstream_rq_non_relative_path.count",
    "http.downstream_rq_overload_close.count",
    "http.downstream_rq_redirected_with_normalized_path.count",
    "http.downstream_rq_response_before_rq_complete.count",
    "http.downstream_rq_rx_reset.count",
    "http.downstream_rq_time.bucket",
    "http.downstream_rq_time.count",
    "http.downstream_rq_time.sum",
    "http.downstream_rq_timeout.count",
    "http.downstream_rq_too_large.count",
    "http.downstream_rq_tx_reset.count",
    "http.downstream_rq_ws_on_non_ws_route.count",
    "http.downstream_rq_xx.count",
    "http.no_cluster.count",
    "http.no_route.count",
    "http.passthrough_internal_redirect_bad_location.count",
    "http.passthrough_internal_redirect_no_route.count",
    "http.passthrough_internal_redirect_predicate.count",
    "http.passthrough_internal_redirect_too_many_redirects.count",
    "http.passthrough_internal_redirect_unsafe_scheme.count",
    "http.rbac_allowed.count",
    "http.rbac_denied.count",
    "http.rbac_shadow_allowed.count",
    "http.rbac_shadow_denied.count",
    "http.rq_direct_response.count",
    "http.rq_redirect.count",
    "http.rq_reset_after_downstream_response_started.count",
    "http.rs_too_large.count",
    "http.tracing.client_enabled.count",
    "http.tracing.health_check.count",
    "http.tracing.not_traceable.count",
    "http.tracing.random_sampling.count",
    "http.tracing.service_forced.count",
    "http.downstream_cx_length_ms.bucket",
    "http.downstream_cx_length_ms.count",
    "http.downstream_cx_length_ms.sum",
    "listener.admin.downstream_cx_active",
    "listener.admin.downstream_cx_destroy.count",
    "listener.admin.downstream_cx_length_ms.bucket",
    "listener.admin.downstream_cx_length_ms.count",
    "listener.admin.downstream_cx_length_ms.sum",
    "listener.admin.downstream_cx_overflow.count",
    "listener.admin.downstream_cx_overload_reject.count",
    "listener.admin.downstream_cx.count",
    "listener.admin.downstream_global_cx_overflow.count",
    "listener.admin.downstream_pre_cx_active",
    "listener.admin.downstream_pre_cx_timeout.count",
    "listener.admin.http.downstream_rq_completed.count",
    "listener.admin.http.downstream_rq_xx.count",
    "listener.admin.no_filter_chain_match.count",
    "listener.downstream_cx_active",
    "listener.downstream_cx_destroy.count",
    "listener.downstream_cx_length_ms.bucket",
    "listener.downstream_cx_length_ms.count",
    "listener.downstream_cx_length_ms.sum",
    "listener.downstream_cx_overflow.count",
    "listener.downstream_cx_overload_reject.count",
    "listener.downstream_cx.count",
    "listener.downstream_global_cx_overflow.count",
    "listener.downstream_pre_cx_active",
    "listener.downstream_pre_cx_timeout.count",
    "listener.http.downstream_rq_completed.count",
    "listener.http.downstream_rq_xx.count",
    "listener.no_filter_chain_match.count",
    "listener_manager.lds.control_plane.connected_state",
    "listener_manager.lds.control_plane.pending_requests",
    "listener_manager.lds.control_plane.rate_limit_enforced.count",
    "listener_manager.lds.init_fetch_timeout.count",
    "listener_manager.lds.update_attempt.count",
    "listener_manager.lds.update_duration.bucket",
    "listener_manager.lds.update_duration.count",
    "listener_manager.lds.update_duration.sum",
    "listener_manager.lds.update_failure.count",
    "listener_manager.lds.update_rejected.count",
    "listener_manager.lds.update_success.count",
    "listener_manager.lds.update_time",
    "listener_manager.lds.version",
    "listener_manager.listener_added.count",
    "listener_manager.listener_create_failure.count",
    "listener_manager.listener_create_success.count",
    "listener_manager.listener_in_place_updated.count",
    "listener_manager.listener_modified.count",
    "listener_manager.listener_removed.count",
    "listener_manager.listener_stopped.count",
    "listener_manager.total_filter_chains_draining",
    "listener_manager.total_listeners_active",
    "listener_manager.total_listeners_draining",
    "listener_manager.total_listeners_warming",
    "listener_manager.workers_started",
    "runtime.admin_overrides_active",
    "runtime.deprecated_feature_seen_since_process_start",
    "runtime.deprecated_feature_use.count",
    "runtime.load_error.count",
    "runtime.load_success.count",
    "runtime.num_keys",
    "runtime.num_layers",
    "runtime.override_dir_exists.count",
    "runtime.override_dir_not_exists.count",
    "server.compilation_settings_fips_mode",
    "server.concurrency",
    "server.days_until_first_cert_expiring",
    "server.debug_assertion_failures.count",
    "server.dynamic_unknown_fields.count",
    "server.envoy_bug_failure.count",
    "server.hot_restart_epoch",
    "server.hot_restart_generation",
    "server.initialization_time_ms.bucket",
    "server.initialization_time_ms.count",
    "server.initialization_time_ms.sum",
    "server.live",
    "server.memory_allocated",
    "server.memory_heap_size",
    "server.memory_physical_size",
    "server.parent_connections",
    "server.seconds_until_first_ocsp_response_expiring",
    "server.state",
    "server.static_unknown_fields.count",
    "server.stats_recent_lookups",
    "server.total_connections",
    "server.uptime",
    "server.version",
    "server.watchdog_mega_miss.count",
    "server.watchdog_miss.count",
    "vhost.vcluster.upstream_rq_retry.count",
    "vhost.vcluster.upstream_rq_retry_limit_exceeded.count",
    "vhost.vcluster.upstream_rq_retry_overflow.count",
    "vhost.vcluster.upstream_rq_retry_success.count",
    "vhost.vcluster.upstream_rq_timeout.count",
    "watchdog_mega_miss.count",
    "watchdog_miss.count",
    "workers.watchdog_mega_miss.count",
    "workers.watchdog_miss.count",
    "cluster.outlier_detection.ejections_active",
    "cluster.outlier_detection.ejections_overflow.count",
    "cluster.outlier_detection.ejections_detected_consecutive_5xx.count",
    "cluster.outlier_detection.ejections_enforced_consecutive_5xx.count",
    "cluster.outlier_detection.ejections_enforced_success_rate.count",
    "cluster.outlier_detection.ejections_detected_success_rate.count",
    "cluster.outlier_detection.ejections_enforced_consecutive_gateway_failure.count",
    "cluster.outlier_detection.ejections_detected_consecutive_gateway_failure.count",
    "cluster.outlier_detection.ejections_enforced_consecutive_local_origin_failure.count",
    "cluster.outlier_detection.ejections_detected_consecutive_local_origin_failure.count",
    "cluster.outlier_detection.ejections_enforced_local_origin_success_rate.count",
    "cluster.outlier_detection.ejections_detected_local_origin_success_rate.count",
    "cluster.outlier_detection.ejections_enforced_failure_percentage.count",
    "cluster.outlier_detection.ejections_detected_failure_percentage.count",
    "cluster.upstream_cx.count",
    "cluster.upstream_cx_http1.count",
    "cluster.upstream_cx_http2.count",
    "cluster.upstream_cx_http3.count",
    "cluster.upstream_cx_rx_bytes.count",
    "cluster.upstream_cx_tx_bytes.count",
    "cluster.upstream_flow_control_backed_up.count",
    "cluster.upstream_flow_control_drained.count",
    "cluster.upstream_flow_control_paused_reading.count",
    "cluster.upstream_flow_control_resumed_reading.count",
    "cluster.upstream_internal_redirect_failed.count",
    "cluster.upstream_internal_redirect_succeeded.count",
    "cluster.upstream_rq_pending.count",
    "cluster.upstream_rq_time.bucket",
    "cluster.upstream_rq_time.count",
    "cluster.upstream_rq_time.sum",
    "http.downstream_cx.count",
    "http.downstream_cx_http1.count",
    "http.downstream_cx_http2.count",
    "http.downstream_cx_http3.count",
    "http.downstream_cx_rx_bytes.count",
    "http.downstream_cx_ssl.count",
    "http.downstream_cx_tx_bytes.count",
    "http.downstream_cx_upgrades.count",
    "http.downstream_flow_control_paused_reading.count",
    "http.downstream_flow_control_resumed_reading.count",
    "http.downstream_rq.count",
    "http.downstream_rq_http1.count",
    "http.downstream_rq_http2.count",
    "http.downstream_rq_http3.count",
    "http.rq.count",
    "vhost.vcluster.upstream_rq.count",
]

LOCAL_RATE_LIMIT_METRICS = [
    "http.local_rate_limit_enabled.count",
    "http.local_rate_limit_enforced.count",
    "http.local_rate_limit_rate_limited.count",
    "http.local_rate_limit_ok.count",
]

RATE_LIMIT_STAT_PREFIX_TAG = 'stat_prefix:http_local_rate_limiter'

FLAKY_METRICS = {
    "listener.downstream_cx_active",
    "listener.downstream_cx_destroy.count",
    "cluster.internal.upstream_rq.count",
    "cluster.internal.upstream_rq_completed.count",
    "cluster.internal.upstream_rq_xx.count",
    "cluster.http2.keepalive_timeout.count",
    "cluster.upstream_rq_xx.count",
    "access_logs.grpc_access_log.logs_written.count",
    "access_logs.grpc_access_log.logs_dropped.count",
}

MOCKED_PROMETHEUS_METRICS = {
    "cluster.assignment_stale.count",
    "cluster.assignment_timeout_received.count",
    "cluster.bind_errors.count",
    "cluster.circuit_breakers.cx_open",
    "cluster.circuit_breakers.cx_pool_open",
    "cluster.circuit_breakers.rq_open",
    "cluster.circuit_breakers.rq_pending_open",
    "cluster.circuit_breakers.rq_retry_open",
    "cluster.default_total_match.count",
    "cluster.external.upstream_rq.count",
    "cluster.external.upstream_rq_completed.count",
    "cluster.external.upstream_rq_time.bucket",
    "cluster.external.upstream_rq_time.count",
    "cluster.external.upstream_rq_time.sum",
    "cluster.external.upstream_rq_xx.count",
    "cluster.http1.dropped_headers_with_underscores.count",
    "cluster.http1.metadata_not_supported_error.count",
    "cluster.http1.requests_rejected_with_underscores_in_headers.count",
    "cluster.http1.response_flood.count",
    "cluster.http2.dropped_headers_with_underscores.count",
    "cluster.http2.header_overflow.count",
    "cluster.http2.headers_cb_no_stream.count",
    "cluster.http2.inbound_empty_frames_flood.count",
    "cluster.http2.inbound_priority_frames_flood.count",
    "cluster.http2.inbound_window_update_frames_flood.count",
    "cluster.http2.outbound_control_flood.count",
    "cluster.http2.outbound_flood.count",
    "cluster.http2.requests_rejected_with_underscores_in_headers.count",
    "cluster.http2.rx_messaging_error.count",
    "cluster.http2.rx_reset.count",
    "cluster.http2.trailers.count",
    "cluster.http2.tx_reset.count",
    "cluster.internal.upstream_rq.count",
    "cluster.internal.upstream_rq_completed.count",
    "cluster.internal.upstream_rq_xx.count",
    "cluster.lb_healthy_panic.count",
    "cluster.lb_local_cluster_not_ok.count",
    "cluster.lb_recalculate_zone_structures.count",
    "cluster.lb_subsets_active",
    "cluster.lb_subsets_created.count",
    "cluster.lb_subsets_fallback.count",
    "cluster.lb_subsets_fallback_panic.count",
    "cluster.lb_subsets_removed.count",
    "cluster.lb_subsets_selected.count",
    "cluster.lb_zone_cluster_too_small.count",
    "cluster.lb_zone_no_capacity_left.count",
    "cluster.lb_zone_number_differs.count",
    "cluster.lb_zone_routing_all_directly.count",
    "cluster.lb_zone_routing_cross_zone.count",
    "cluster.lb_zone_routing_sampled.count",
    "cluster.max_host_weight",
    "cluster.membership_change.count",
    "cluster.membership_degraded",
    "cluster.membership_excluded",
    "cluster.membership_healthy",
    "cluster.membership_total",
    "cluster.original_dst_host_invalid.count",
    "cluster.retry_or_shadow_abandoned.count",
    "cluster.update_attempt.count",
    "cluster.update_empty.count",
    "cluster.update_failure.count",
    "cluster.update_no_rebuild.count",
    "cluster.update_success.count",
    "cluster.upstream_cx.count",
    "cluster.upstream_cx_active",
    "cluster.upstream_cx_close_notify.count",
    "cluster.upstream_cx_connect_attempts_exceeded.count",
    "cluster.upstream_cx_connect_fail.count",
    "cluster.upstream_cx_connect_ms.bucket",
    "cluster.upstream_cx_connect_ms.count",
    "cluster.upstream_cx_connect_ms.sum",
    "cluster.upstream_cx_connect_timeout.count",
    "cluster.upstream_cx_destroy.count",
    "cluster.upstream_cx_destroy_local.count",
    "cluster.upstream_cx_destroy_local_with_active_rq.count",
    "cluster.upstream_cx_destroy_remote.count",
    "cluster.upstream_cx_destroy_remote_with_active_rq.count",
    "cluster.upstream_cx_destroy_with_active_rq.count",
    "cluster.upstream_cx_http1.count",
    "cluster.upstream_cx_http2.count",
    "cluster.upstream_cx_idle_timeout.count",
    "cluster.upstream_cx_length_ms.bucket",
    "cluster.upstream_cx_length_ms.count",
    "cluster.upstream_cx_length_ms.sum",
    "cluster.upstream_cx_max_requests.count",
    "cluster.upstream_cx_none_healthy.count",
    "cluster.upstream_cx_overflow.count",
    "cluster.upstream_cx_pool_overflow.count",
    "cluster.upstream_cx_protocol_error.count",
    "cluster.upstream_cx_rx_bytes.count",
    "cluster.upstream_cx_rx_bytes_buffered",
    "cluster.upstream_cx_tx_bytes.count",
    "cluster.upstream_cx_tx_bytes_buffered",
    "cluster.upstream_flow_control_backed_up.count",
    "cluster.upstream_flow_control_drained.count",
    "cluster.upstream_flow_control_paused_reading.count",
    "cluster.upstream_flow_control_resumed_reading.count",
    "cluster.upstream_internal_redirect_failed.count",
    "cluster.upstream_internal_redirect_succeeded.count",
    "cluster.upstream_rq.count",
    "cluster.upstream_rq_active",
    "cluster.upstream_rq_cancelled.count",
    "cluster.upstream_rq_completed.count",
    "cluster.upstream_rq_maintenance_mode.count",
    "cluster.upstream_rq_pending.count",
    "cluster.upstream_rq_pending_active",
    "cluster.upstream_rq_pending_failure_eject.count",
    "cluster.upstream_rq_pending_overflow.count",
    "cluster.upstream_rq_per_try_timeout.count",
    "cluster.upstream_rq_retry.count",
    "cluster.upstream_rq_retry_limit_exceeded.count",
    "cluster.upstream_rq_retry_overflow.count",
    "cluster.upstream_rq_retry_success.count",
    "cluster.upstream_rq_rx_reset.count",
    "cluster.upstream_rq_time.bucket",
    "cluster.upstream_rq_time.count",
    "cluster.upstream_rq_time.sum",
    "cluster.upstream_rq_timeout.count",
    "cluster.upstream_rq_tx_reset.count",
    "cluster.upstream_rq_xx.count",
    "cluster.version",
    "cluster_manager.active_clusters",
    "cluster_manager.cds.control_plane.connected_state",
    "cluster_manager.cds.control_plane.pending_requests",
    "cluster_manager.cds.control_plane.rate_limit_enforced.count",
    "cluster_manager.cds.init_fetch_timeout.count",
    "cluster_manager.cds.update_attempt.count",
    "cluster_manager.cds.update_failure.count",
    "cluster_manager.cds.update_rejected.count",
    "cluster_manager.cds.update_success.count",
    "cluster_manager.cds.update_time",
    "cluster_manager.cds.version",
    "cluster_manager.cluster_added.count",
    "cluster_manager.cluster_modified.count",
    "cluster_manager.cluster_removed.count",
    "cluster_manager.cluster_updated.count",
    "cluster_manager.custer_updated_via_merge.count",
    "cluster_manager.update_merge_cancelled.count",
    "cluster_manager.update_out_of_merge_window.count",
    "cluster_manager.warming_clusters",
    "filesystem.flushed_by_timer.count",
    "filesystem.reopen_failed.count",
    "filesystem.write_buffered.count",
    "filesystem.write_completed.count",
    "filesystem.write_failed.count",
    "filesystem.write_total_buffered",
    "http.downstream_cx.count",
    "http.downstream_cx_active",
    "http.downstream_cx_delayed_close_timeout.count",
    "http.downstream_cx_destroy.count",
    "http.downstream_cx_destroy_active_rq.count",
    "http.downstream_cx_destroy_local.count",
    "http.downstream_cx_destroy_local_active_rq.count",
    "http.downstream_cx_destroy_remote.count",
    "http.downstream_cx_destroy_remote_active_rq.count",
    "http.downstream_cx_drain_close.count",
    "http.downstream_cx_http1.count",
    "http.downstream_cx_http1_active",
    "http.downstream_cx_http2.count",
    "http.downstream_cx_http2_active",
    "http.downstream_cx_http3.count",
    "http.downstream_cx_http3_active",
    "http.downstream_cx_idle_timeout.count",
    "http.downstream_cx_length_ms.bucket",
    "http.downstream_cx_length_ms.count",
    "http.downstream_cx_length_ms.sum",
    "http.downstream_cx_max_duration_reached.count",
    "http.downstream_cx_overload_disable_keepalive.count",
    "http.downstream_cx_protocol_error.count",
    "http.downstream_cx_rx_bytes.count",
    "http.downstream_cx_rx_bytes_buffered",
    "http.downstream_cx_ssl.count",
    "http.downstream_cx_ssl_active",
    "http.downstream_cx_tx_bytes.count",
    "http.downstream_cx_tx_bytes_buffered",
    "http.downstream_cx_upgrades.count",
    "http.downstream_cx_upgrades_active",
    "http.downstream_flow_control_paused_reading.count",
    "http.downstream_flow_control_resumed_reading.count",
    "http.downstream_rq.count",
    "http.downstream_rq_active",
    "http.downstream_rq_completed.count",
    "http.downstream_rq_http1.count",
    "http.downstream_rq_http2.count",
    "http.downstream_rq_http3.count",
    "http.downstream_rq_idle_timeout.count",
    "http.downstream_rq_max_duration_reached.count",
    "http.downstream_rq_non_relative_path.count",
    "http.downstream_rq_overload_close.count",
    "http.downstream_rq_response_before_rq_complete.count",
    "http.downstream_rq_rx_reset.count",
    "http.downstream_rq_time.bucket",
    "http.downstream_rq_time.count",
    "http.downstream_rq_time.sum",
    "http.downstream_rq_timeout.count",
    "http.downstream_rq_too_large.count",
    "http.downstream_rq_tx_reset.count",
    "http.downstream_rq_ws_on_non_ws_route.count",
    "http.downstream_rq_xx.count",
    "http.no_cluster.count",
    "http.no_route.count",
    "http.rbac_allowed.count",
    "http.rbac_denied.count",
    "http.rbac_shadow_allowed.count",
    "http.rbac_shadow_denied.count",
    "http.local_rate_limit_enabled.count",
    "http.local_rate_limit_enforced.count",
    "http.local_rate_limit_rate_limited.count",
    "http.local_rate_limit_ok.count",
    "http.rq.count",
    "http.rq_direct_response.count",
    "http.rq_redirect.count",
    "http.rq_reset_after_downstream_response_started.count",
    "http.rs_too_large.count",
    "http.tracing.client_enabled.count",
    "http.tracing.health_check.count",
    "http.tracing.not_traceable.count",
    "http.tracing.random_sampling.count",
    "http.tracing.service_forced.count",
    "listener.admin.downstream_cx.count",
    "listener.admin.downstream_cx_active",
    "listener.admin.downstream_cx_destroy.count",
    "listener.admin.downstream_cx_length_ms.bucket",
    "listener.admin.downstream_cx_length_ms.count",
    "listener.admin.downstream_cx_length_ms.sum",
    "listener.admin.downstream_pre_cx_active",
    "listener.admin.downstream_pre_cx_timeout.count",
    "listener.admin.http.downstream_rq_completed.count",
    "listener.admin.http.downstream_rq_xx.count",
    "listener.admin.no_filter_chain_match.count",
    "listener.downstream_cx.count",
    "listener.downstream_cx_active",
    "listener.downstream_cx_destroy.count",
    "listener.downstream_cx_length_ms.bucket",
    "listener.downstream_cx_length_ms.count",
    "listener.downstream_cx_length_ms.sum",
    "listener.downstream_pre_cx_active",
    "listener.downstream_pre_cx_timeout.count",
    "listener.http.downstream_rq_completed.count",
    "listener.http.downstream_rq_xx.count",
    "listener.no_filter_chain_match.count",
    "listener_manager.lds.control_plane.connected_state",
    "listener_manager.lds.control_plane.pending_requests",
    "listener_manager.lds.control_plane.rate_limit_enforced.count",
    "listener_manager.lds.init_fetch_timeout.count",
    "listener_manager.lds.update_attempt.count",
    "listener_manager.lds.update_failure.count",
    "listener_manager.lds.update_rejected.count",
    "listener_manager.lds.update_success.count",
    "listener_manager.lds.update_time",
    "listener_manager.lds.version",
    "listener_manager.listener_added.count",
    "listener_manager.listener_create_failure.count",
    "listener_manager.listener_create_success.count",
    "listener_manager.listener_modified.count",
    "listener_manager.listener_removed.count",
    "listener_manager.listener_stopped.count",
    "listener_manager.total_listeners_active",
    "listener_manager.total_listeners_draining",
    "listener_manager.total_listeners_warming",
    "listener_manager.workers_started",
    "runtime.admin_overrides_active",
    "runtime.deprecated_feature_use.count",
    "runtime.load_error.count",
    "runtime.load_success.count",
    "runtime.num_keys",
    "runtime.num_layers",
    "runtime.override_dir_exists.count",
    "runtime.override_dir_not_exists.count",
    "server.concurrency",
    "server.days_until_first_cert_expiring",
    "server.debug_assertion_failures.count",
    "server.dynamic_unknown_fields.count",
    "server.hot_restart_epoch",
    "server.hot_restart_generation",
    "server.initialization_time_ms.bucket",
    "server.initialization_time_ms.count",
    "server.initialization_time_ms.sum",
    "server.live",
    "server.memory_allocated",
    "server.memory_heap_size",
    "server.memory_physical_size",
    "server.parent_connections",
    "server.state",
    "server.static_unknown_fields.count",
    "server.stats_recent_lookups",
    "server.total_connections",
    "server.uptime",
    "server.version",
    "server.watchdog_mega_miss.count",
    "server.watchdog_miss.count",
    "vhost.vcluster.upstream_rq.count",
    "vhost.vcluster.upstream_rq_retry.count",
    "vhost.vcluster.upstream_rq_retry_limit_exceeded.count",
    "vhost.vcluster.upstream_rq_retry_overflow.count",
    "vhost.vcluster.upstream_rq_retry_success.count",
    "vhost.vcluster.upstream_rq_timeout.count",
    "access_logs.grpc_access_log.logs_dropped.count",
    "access_logs.grpc_access_log.logs_written.count",
    "tcp.downstream_cx.count",
    "tcp.downstream_cx_no_route.count",
    "tcp.downstream_cx_rx_bytes.count",
    "tcp.downstream_cx_rx_bytes_buffered",
    "tcp.downstream_cx_tx_bytes.count",
    "tcp.downstream_cx_tx_bytes_buffered",
    "tcp.downstream_flow_control_resumed_reading.count",
    "tcp.idle_timeout.count",
    "tcp.on_demand_cluster_attempt.count",
    "tcp.on_demand_cluster_missing.count",
    "tcp.on_demand_cluster_success.count",
    "tcp.on_demand_cluster_timeout.count",
    "tcp.upstream_flush.count",
    "tcp.upstream_flush_active",
}


def get_fixture_path(filename):
    return os.path.join(HERE, 'fixtures', filename)
