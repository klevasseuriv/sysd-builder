# sysd-builder
Systemd Service Builder

I made this because I got tired of copying templates and looking up syntax/correct service file locations every time I needed some command to run as a service or on a schedule.
Theres's a lot of options for systemd services and this is not designed to fit everyone's use case. I just found that 99% of the time I was typing the same five lines.

Usage:
```
sudo sdb --name myservice --cmd "my-command --arg1 --arg2 'something in quotes'" --service-type oneshot
```

TODO:
- User/system flag
- Timers
- Service type enums
- Other minor args (restart, execstop etc.)
