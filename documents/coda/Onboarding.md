Welcome to the Data Science team! 👋 🥳  

This page outlines guidance for new joiners (Data Scientists and Data Engineers) to get started with relevant links and topics.

## Getting Started 🥇

- Join any relevant Slack channels (discuss with you colleagues to get an up-to-date list):
  - [#ds-and-mle](https://intent.slack.com/archives/C036BAE7R3N) - public channel for the core DS and MLE teams
  - [#data_science](https://intent.slack.com/archives/CDPTU197B) - public channel for wider-audience data discussions, includes the applied DS team and many non-DS people
  - #core_data_science  - private channel for the core DS team, ask anyone in the team for an invite
  - [#journalclub](https://intent.slack.com/archives/C02MX7FQWA3) - public channel for posting interesting papers and organising the [Journal Club](https://coda.io/d/_dK5h4iVEEUo/_suKD3#_luxbk)
  - [#mle-geekouts](https://intent.slack.com/archives/C0532S269UH)  -  private channel for the  [https://coda.io/d/_dK5h4iVEEUo/_suUzL#_luptV](https://coda.io/d/_dK5h4iVEEUo/_suUzL#_luptV)
  - #ai-products - main team channel
  - #ai-products-team-stuff - internal team channel
  - #data-science-function
- Add your row to the Team Sheet on [https://coda.io/d/_dK5h4iVEEUo/_sufdJ#_luM-F](https://coda.io/d/_dK5h4iVEEUo/_sufdJ#_luM-F)
- Confirm you have been included in regular team events and ceremonies (ask [Nidhi Sharma](mailto:nidhi.sharma@intenthq.com) for invites)
  - DS: daily stand ups, sprint review and retro, DS shindig, journal club
  - MLE: deep dives & geek outs, daily stand ups) 
- Familiarise yourself with key terms and acronyms - checkout our [https://coda.io/d/_dK5h4iVEEUo/_sub60](https://coda.io/d/_dK5h4iVEEUo/_sub60)
- Read and sign our client NDAs
  - You will be notified by email.
  - This comes after a few weeks.

## Software to Install 💾

Find a list of some relevant tools below

| Name | Notes | Column 3 |
| --- | --- | --- |
| IDE | The team prefer using **pycharm** for python and IntelliJ for Java and Scala but the team also includes atom and VS code users |  |
| Command Line Tools | Command Line Tools is very useful and will install lots of useful things for you (like git!). You can install the tools by running:<br/><br/>```<br/>xcode-select --install<br/>``` |  |
| Git | If you install Command Line Tools, git gets automatically installed. <br/><br/>For git access, see Platform access below.<br/><br/>To enable git auto-complete:<br/><br/>**bash**:<br/><br/>Download the script:<br/><br/>```<br/>curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash<br/>```<br/><br/>Then add this to ~/.bash_profile<br/><br/>```<br/>if [ -f ~/.git-completion.bash ]; then<br/>  . ~/.git-completion.bash<br/>fi<br/>```<br/><br/>**zsh**:<br/><br/>```<br/>`echo` `'autoload -Uz compinit && compinit'` `>> ~/.zshrc`<br/>```<br/><br/> |  |
| Python | Latest version available [here](https://www.python.org/downloads/macos/) |  |
| Aviatrix VPN Client | Available via Intent HQ self service portal |  |
| Zoom | Available via Intent HQ self service portal |  |
| Slack | Available via Intent HQ self service portal |  |
| OKTA verify | MFA mobile application of choice (available for iOS and Android) |  |
| CyberDuck | File transfer client |  |
| Loom | Screen Recording - available via Intent HQ self service portal |  |
| Internet Browser | Available via Intent HQ self service portal |  |
| Atom | [https://atom.io/](https://atom.io/) |  |
| Citrix workspace | Available [here](https://www.citrix.com/en-gb/downloads/workspace-app/mac/workspace-app-for-mac-latest.html). Only if you will be accessing the Verizon platform |  |




## Platform Accesses 🔒

### GitHub

We use GitHub for version control using git.

As of February 2023, there are two things you need to get access to our git repositories:

- **(1) A UAM ticket sent by your manager**

An access request should be included in an UAM ticket sent by your manager, so make sure your manager sent that. This request will need the following:

- Your GitHub profile (either linking your personal GitHub or creating a new account using your Intent HQ email)
- Specify you would like to be added to the **data science group**, you will be added to the data science group giving you access to the majority of our repos (you may still need to request access to repos owned by other teams i.e. `pipeline-process` )
- **(2) Go to Opal.dev**

For any source code access, you need to use [Opal.dev](Opal.dev) (accessible from Okta plugin on your browser). In Opal.dev:

  - First connect your github account in settings ([https://app.opal.dev/user/settings](https://app.opal.dev/user/settings)) *****
  - Then in Resources section, you can request access to the Data Science github group. That gets sent to the respective approvers 
  - If you need access to other repos, you can request access to those as well.

After that, you will need to accept the invitation pending in your github account.

***** If you use your personal git profile, you will need to to add your IHQ email address as your secondary email to your Github profile.



*If you have issues with this process, you can get in touch with @**[Evgeny Lazarev](https://app.slack.com/team/U024Y4W4R)* 



Before you can clone any Github projects you must add your ssh key to the account, please find some relevant links below

- [Generating an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Adding an SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
- [Cloning a Repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

### Other Platforms

Your line manager should have submitted a User Access Management (UAM) ticket for your other platform accesses

You can check out the portal [here](https://intenthq.atlassian.net/servicedesk/customer/portal/6) - you may be granted access right-away since they are working their way through the ticket

An example of the ticket and the accesses requested is shown in the below image for reference





**Databricks - Florela/Manuel to update**

1. **NDA’s**
2. **Raise UAM for accessing ML**

## Setting up the local environment 💻

[Follow this doc for setting up your local environment](https://intenthq.slab.com/posts/setting-up-the-local-environment-%F0%9F%92%BB-eel5yqc4)

This article also covers configurations required for docker, SSH config and tunnelling, choosing the editor for development, and Insomnia config.

### Troubleshooting when you run `local-env/setup`
| Step | Issue | Solution |
| --- | --- | --- |
| sdkmanInstall | java versions not found for M1 chips | check out t[his guide](https://itnext.io/how-to-install-x86-and-arm-jdks-on-the-mac-m1-apple-silicon-using-sdkman-872a5adc050d) for installing through SDKMAN on Apple Silicon. You may need to run `source "$HOME/.sdkman/bin/sdkman-init.sh`" in the same terminal window before running the setup script to ensure it works |
| homebrew | docker installed failed for M1 chips | remove ln36 `cask docker` from the Brewfile[There is a separate distro for Apple Silicon](https://docs.docker.com/desktop/mac/apple-silicon/) |
| npmPackages |  | Despite the fact that Brewfile includes `node@12`, you may need to run `brew install node` before the npm package install will work correctly. |
| sshStuff |  | The permissions/ownership of `/usr/local/bin` aren’t compatible with the script. I cheated and ran this outside the script:<br/><br/>```<br/>sudo su -<br/>cd ~/<path to parent of hello><br/>sed "s\|{IHQ_WORKDIR}\|$(pwd)\|" hello/local-env/bin/fssh.template > "/usr/local/bin/fssh"<br/>sed "s\|{IHQ_WORKDIR}\|$(pwd)\|" hello/local-env/bin/fautossh.template > "/usr/local/bin/fautossh"<br/>exit<br/>pushd .. <br/>sudo chmod u+x /usr/local/bin/fssh<br/>sudo chmod u+x /usr/local/bin/fautossh <br/>sed "s\|{IHQ_WORKDIR}\|$(pwd)\|" hello/local-env/ssh/config > ~/.ssh/ihq-config<br/>popd<br/>``` |
| symlinkBins |  |  |
| clone internal Repos | ❌ Failed to run command 'git clone --recurse-submodules git@github.com:intenthq/config-validations.git' with status code '128'! | remove `”deployments”` from the setup since this repo is outside of scope. (Open in TextEdit, if you have no other IDE installed)  <br/>You might find also that `config-validations` cause an error as the repo can’t be found.  <br/>  <br/>**NOTE:** you can also remove any repos you have already cloned. |
| running brew | ❌ Failed to run command 'brew bundle --file=local-env/Brewfile' with status code '127'!  | Install brew manually, following: <br/><br/>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"<br/><br/>Add into shell:<br/><br/>echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile<br/><br/>eval "$(/opt/homebrew/bin/brew shellenv)"<br/><br/> |
| Installing docker credentails | ==> ⏳ Installing docker-credential-helper-ecr<br/>==> ⏳ Copying docker/config.json<br/>==> ❌ Failed to run command 'cp /Users/.../Documents/hello/local-env/docker/config.json /Users/.../.docker/config.json' with status code '1'! | create a .docker folder: mkdir .docker |
| **General** |  |  |


## ~~Setting up AWS roles~~

This process - accessing AWS via Okta - still works but is about to be deprecated. See the next section on the more up-to-date and recommended way.

This browser extension will make it easier to switch roles and accounts when logged into the AWS console. You can set it up before getting access to AWS but you won’t be able to use it. 

Install the [AWS Switch Roles](https://github.com/tilfin/aws-extend-switch-roles) extension.

Open its “Options”





Add the config from [here](https://github.com/intenthq/hello/blob/master/local-env/assets/aws-extend-switch-roles.txt).

Then use the extension, not the role switch drop-down on the AWS page, for switching. Note that automatically setting the region doesn’t always work.

You can do the same in Citrix, or just use the built-in Switch Role and copy the values for VZW from this config the first time.

Note that the configuration may includes accounts that you will not have access to. In this case, clicking the role will lead to a screen that looks like the one below. This means you cannot actually select it - or that you are in the wrong main AWS account (currently only applicable to Orange Spain).



## Accessing AWS via Opal

Accessing AWS:

- Go to **Opal.dev** through Okta (e.g. via the plugin)
  - 
- Go to **AWS IntentHQ** in **Apps**
  - 
- Go to the environment you need access to, e.g. intenthq-verizon
  - For demo/setup purposes, you can select **IntentHQ Development**, which is the dev environment
- Select the **Engineer** role (this is the permissions closest to our requirements)
- Click **Request** and submit a request
  - 
  - For the dev environment, it should auto-approve for you
  - Client environment will need a human to approve the request, but it should typically take just a few minutes
- Then go back through the same pathway Apps → IntentHQ Development → Engineer and click **Connect** this will open AWS in an authenticated window for you
  - 
- Click the **Access AWS Console** to open the console in a new tab
  - 
  - Or copy and paste the `opal` command in your terminal to authenticate there (if you need command line AWS access)
    - You might need to install the Opal CLI first: `brew install opalsecurity/brew/opal-security`
- Note: The access will timeout after 1hr, you can restart this by reconnecting through Opal and refreshing your old tab

## Setting up Insights Explorer 🔷

All the information for setting up Insights Explorer can be found following these documents

1. [Run pipeline from local environment](https://intenthq.slab.com/posts/local-environment-7ax55e1h)
2. [Run config services locally](https://intenthq.slab.com/posts/how-to-run-config-service-locally-nh6pcbk2)
3. [Setup the dashboard API locally](https://github.com/intenthq/insights-explorer/blob/master/api/README.md#quickstart-runningrunningrunning)

## Key People & Contacts 🧑‍🤝‍🧑

| Name | Title | Primary Contact for... |
| --- | --- | --- |
| Kumutha Swampillai | Director of Data Science | Data Science Backlog |
| Andy Cole | Global Director of Applied Data Science & Analytics |  |
| Gareth Jones | IT Manager | For IT related queries |
| Evgeny Lazarev | Head of Cyber Security | For access to Github |
| Alex Murphy | Global People Team Coordinator | For General Onboarding and People Queries |
|  |  | For Learning and Development queries |
| Kevin Magee | CTO |  |
| Harvey Yau | Head of Technical Operations | @techops on Slack for general ops support. Harvey direct if you need the big guns for something infrastructure related |
| Cat |  | Data Sources across all clients  <br/>Support for Engineering or Ops issues for Data Science |
| Alex Silver |  | Brand Affinity Algorithm  <br/>Anything O2 Data Science related  <br/> |






## Handy Bookmarks ⭐

Find a list of handy links to bookmarks for your internet browser here

| Link | Notes |
| --- | --- |
| [Daily Check-in](https://coda.io/d/IHQ-Remote_dL66B7SW8ok/Team-Roster_suIaR#_lubJS) | direct link to coda page for daily check in |
| [Coda](https://coda.io/workspaces/ws-MbR90oAKSM/docs?tour=new-user-multiple-workspaces) | [coda.io](coda.io) for documentation |
| [Calendar](https://calendar.google.com/calendar/u/0/r?tab=mc&pli=1) | Google Calendar |
| [Inbox](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox) | GMail |
| [Atlassian \| Start page](https://start.atlassian.com/) | Landing page for UAM and Jira instance |
| [Slab](https://intenthq.slab.com/) | Slab for documentation |
| [NINJIO](https://dojo.ninjio.com/Modules/User/Login.aspx?returnurl=/Modules/Default.aspx) | Security training platform |
| [UAM](https://intenthq.atlassian.net/servicedesk/customer/portal/6/user/login?destination=portal%2F6%2FUAM-1441) | User Access Management - for raising tickets |
| [HiBob](https://app.hibob.com/home) | For logging annual leave and sickness |
| [Teamtailor](https://app.teamtailor.com/companies/4iW4IlfJytM/employee) | Recruitment platform |
| [Miro](https://miro.com/app/board/uXjVONubcpw=/) | White-boarding colab tool |
| [GitHub](https://github.com/) | codebase |
| [OKTA](https://intenthq.okta.com/app/UserHome) | SSO |
| [IHQ hub](http://ihqhub.intenthq.com/) | IHQ managed bookmarks |




## Useful Resources 🗂

A list of files and pages to also check out

| Resource | Description | Where to find it |
| --- | --- | --- |
| Data Platform Deep-Dive slides | An in-depth look at out data platform; marketable benefits and how they are technically achieved |  |
| generic tech overview | slides on some of the benefits of our data platform opposed to generic market offerings |  |


## 

## People, sick days, holidays, training

[https://app.hibob.com/login/home](https://app.hibob.com/login/home) 

Hibob is the platform which addresses all of the above, you just locate the request time off and fill out accordingly



## Help improve this document 🙌

Please actively contribute this document with new learnings or relevant material

list any areas that you feel should be included as part of this document 👇

- AWS Configuration (AWS vault?) - **follow up with Manuel about this ***role setup added, not sure if there’s anything else missing?