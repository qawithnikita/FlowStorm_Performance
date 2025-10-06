ORG_CONFIG = {
  "configs": [
    {
      "config": {
        "amplitude": {
          "session_replay_enabled": True,
          "session_replay_sample_rate": 0.05,
          "tracking_enabled": True
        },
        "datadog": {
          "default_privacy_level": "allow",
          "logs_enabled": False,
          "rum_enabled": False,
          "session_replay_enabled": False,
          "session_replay_sample_rate": 100,
          "session_sample_rate": 100,
          "trace_sample_rate": 100
        }
      },
      "created_at": "2025-02-10T17:00:00.133910+00:00",
      "id": "c785e06f-fbb9-4d31-b85e-bca12af26553",
      "is_latest": True,
      "namespace": "test-react-components",
      "organization_id": "f7c4050e-0dd1-4dd1-a50e-4809573009a8",
      "updated_at": "2025-02-12T14:20:00.133910+00:00",
      "updated_by_entity": "api_key",
      "updated_by_entity_id": "7412551f-6bd0-4260-8b7a-654e8f9f5e64",
      "version": "1.0.0"
    }
  ],
  "experiments": [
    {
      "group": None,
      "group_name": None,
      "name": "default",
      "rule_id": None,
      "value": {}
    }
  ],
  "gates": [
    {
      "group_name": None,
      "name": "is_client_session_enabled",
      "rule_id": None,
      "value": False
    },
    {
      "group_name": None,
      "name": "is_new_feature_enabled",
      "rule_id": None,
      "value": False
    },
    {
      "group_name": None,
      "name": "is_fine_tuned_model_8b",
      "rule_id": None,
      "value": False
    },
    {
      "group_name": None,
      "name": "is_integrated_cx_enabled",
      "rule_id": None,
      "value": False
    },
    {
      "group_name": None,
      "name": "is_non_shapewear_enabled",
      "rule_id": None,
      "value": True
    },
    {
      "group_name": None,
      "name": "is_force_injection_enabled",
      "rule_id": None,
      "value": False
    },
    {
      "group_name": None,
      "name": "is_image_banner_enabled",
      "rule_id": None,
      "value": False
    },
    {
      "group_name": None,
      "name": "is_search_hash_enabled",
      "rule_id": None,
      "value": False
    }
  ],
  "org": {
    "org": {
      "created_at": "2025-02-10T17:00:00.133910+00:00",
      "display_name": "MyMerchant",
      "domain": "my-merchant.com",
      "id": "f7c4050e-0dd1-4dd1-a50e-4809573009a8",
      "short_name": "my-merchant",
      "status": "active",
      "updated_at": "2025-02-12T14:20:00.133910+00:00"
    },
    "settings": {}
  }
}
