# Changelog

All notable changes to this project will be documented in this file.
By "notable", we mean, at the very least, user visible changes will be documented.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Or at least, from 1.1.0 on, it will try to adhere to SemVer.


## [1.1.0] - 2026-27-May

### Added

- Skip tests marked with `@pytest.mark.hugemem` by default.  
  - `--hugemem` and `--run-hugemem` allows you to run above tests.
  - Thanks [@neutrinoceros](https://github.com/neutrinoceros) 

## [1.0] - 2026-27-May

### Added
- `--run-slow` alias to mean the same thing as `--slow`, run the tests marked `@pytest.mark.slow`.

### Changed

- A bunch of updates and merges from Clément Robert[@neutrinoceros](https://github.com/neutrinoceros).
  - Thanks Clément 


## [0.0.2 through 0.0.5] - 2021-28-Sept through 2023-09-Feb

- Basic functionality available
- I'm honestly not sure what went in which release.
- Odds are it was done in 2021, and other releases updated which Python versions to test against.
  - And I'm too lazy to look that up and it doesn't really matter. 
  - Just use 1.1.0 or later. :)