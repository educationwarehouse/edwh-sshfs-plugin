# Changelog

<!--next-version-placeholder-->

## v0.1.3 (2023-06-09)
### Fix
* Plumbum sshfs import could still give a sshfs import error. this is due to it for some reason not always giving a commandNotFound ([`0100f8f`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/0100f8fa9ec664f1a07a269e8c89873560dbd139))

## v0.1.2 (2023-05-31)
### Fix
* **import:** Don't crash the entire edwh tool if sshfs is not installed! ([`03b8365`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/03b836576b36d3c814a9678ad0b98fd12a7e246f))

## v0.1.1 (2023-05-25)
### Fix
* Set umask to highest permission level ([`c8c7362`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/c8c7362b8ea77c0ec62672bdaaa798b388806c89))
* Pytest use anyio instead of anyio now. also events are used now instead of queue's for simplicity and added allow root instead of allow other ([`6c002b6`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/6c002b681e77a6f31ee135468bf541601b0e5a55))
* Pytest use anyio instead of anyio now. also events are used now instead of queue's for simplicity ([`913f135`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/913f135e167bf83f5bec3ce6340c81c2e85f75f3))
* Added umask and removed ro because ro is (read-only) ([`3f63ff0`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/3f63ff0c7fde0b21b1e369cbf3693c60252ad6dd))
* Added ro ([`0d9e27d`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/0d9e27daa3eb31f7c28c4129869675cd530562ab))
* Making sure permissions are r&w ([`16b48e0`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/16b48e00a64289280e66debd14148ed95647e265))
* Double -o ([`45ef167`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/45ef1670a8a7751fba0b9b01a025976d596dffc4))
* Permissions ([`88ca0a7`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/88ca0a7d13fe602b607d0575a14a7ac8bf0cce50))
* Added sshfs to dependencies ([`f91791c`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/f91791c2492b3f52c35c578e4b80ae99b0633b77))
* Async doesn't work and is now splitsed into 2 different function sync and async ([`2e15501`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/2e15501629cd478415f04b1151a5e908cd2797a0))
* Help didn't have ':' again ([`55e21b9`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/55e21b9bf232f38c4cb7cad3df49c8c214783bc3))
* Help didn't have ':' ([`fc36466`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/fc36466f06e883df0fb98b9a6e7c60fdcae291dd))
* All tests are working now, queue added to arguments and need to be removed from the cli ([`4655d7a`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/4655d7aabcf85f135e31a0948290ce884c4dfef0))

### Documentation
* Added auto reboot when installing sshfs ([`8b90d1f`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/8b90d1ff49e864c50814b6f929f79ee8675d98e3))
* Added sshfs to install ([`ec35c80`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/ec35c80f6886157643b076d32d24f7bb6ff4dbab))
* Updated install guide ([`60c03ff`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/60c03ffc1c3a294243cbd8419a9078f086816583))
* Updated README.md, added links ([`6b06d6c`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/6b06d6c3208d00fa8a72be427d049200d49b7f75))
* Updated README.md ([`62c3549`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/62c35499d8542aace4df77880528603ed0307c14))
* Updated fabfile.py docs ([`a362d36`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/a362d369ca86bbd921829ea0b66e539304e64e39))
* Updated README.md ([`70d072a`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/70d072aeff696b79ef7193686189eefbecd98d24))

## v0.1.0 (2023-05-19)
### Feature
* Added remote-mount, this will like the name says make an remote mount that makes sure the remote and local files are the same. rn there is still a bit of a delay until something updates, however that is something for the future. ([`29aa07f`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/29aa07fcba70723e9a8930ff852284d0a075ad7e))
* Added get_available_port function ([`a0e77a0`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/a0e77a06a2e6758fa6b11ea321f1a623535274fd))

### Fix
* Removed local umount because sshfs does it automatically ([`1f18a6b`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/1f18a6b24503e21dc7756e39e3fa92138f9a9639))
* Attempt to unmount local_mount when exiting + some code duplication cleanup ([`8793281`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/879328168e8fec0f96500be9903279f9c1ff0095))
* Small peformance improvements with auto_cash and reconnect enabled. down from more then 5s to 2s ([`bf3e1b0`](https://github.com/educationwarehouse/edwh-sshfs-plugin/commit/bf3e1b0419a489d35bc746980c0d8db91c8b1a3f))