# Changelog

<!--next-version-placeholder-->

## v0.1.0 (2023-05-19)
### Feature
* Added remote-mount, this will like the name says make an remote mount that makes sure the remote and local files are the same. rn there is still a bit of a delay until something updates, however that is something for the future. ([`29aa07f`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/29aa07fcba70723e9a8930ff852284d0a075ad7e))
* Added get_available_port function ([`a0e77a0`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/a0e77a06a2e6758fa6b11ea321f1a623535274fd))

### Fix
* Removed local umount because sshfs does it automatically ([`1f18a6b`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/1f18a6b24503e21dc7756e39e3fa92138f9a9639))
* Attempt to unmount local_mount when exiting + some code duplication cleanup ([`8793281`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/879328168e8fec0f96500be9903279f9c1ff0095))
* Small peformance improvements with auto_cash and reconnect enabled. down from more then 5s to 2s ([`bf3e1b0`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/bf3e1b0419a489d35bc746980c0d8db91c8b1a3f))