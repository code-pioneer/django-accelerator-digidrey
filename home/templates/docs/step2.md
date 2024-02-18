## Setup OAuth

#### Create Credentials

1. Login to your Google account.
2. Visit [https://console.cloud.google.com/apis/dashboard](https://console.cloud.google.com/apis/dashboard)
3. From sidebar menu, select `Credentials` (key icon)
4. Click on `+ CREATE CREDENTIALS` and select `OAuth Client ID`
5. Application type: Web application
6. Name: Give a meaningful name
7. Authorized redirect URIs: Click on `+ ADD URI` and set `http://localhost:8000/accounts/google/login/callback/`. Add another entry `http://127.0.0.1:8000/accounts/google/login/callback/`. 
7. Leave everything default during development and select Create.
8. Record `Client ID` and `Secret Key`.

#### Configure Django Administration

1. Login using your admin crudential (established during setup process)
2. Click on `Social applications` under SOCIAL ACCOUNTS section
3. On the right-top corner, click on `ADD SOCIAL APPLICATION +` button.
4. Provider: Select `Google` from 'Provider' dropdown
5. Provider ID: Give a name (preferably same name that you created in Google OAuth Configuration)
6. Name: Keep same as provier id 
7. Client id: Set the value you obtain from OAuth Configuration
8. Secret key: Set the value you obtain from OAuth Configuration
9. Key & Settings: Keep default values provided
10. Sites: Add available sites
11. Click on Save. Settings should picked up immediately. 