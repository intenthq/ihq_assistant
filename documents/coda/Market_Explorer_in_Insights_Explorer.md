# **Background**

Our Market Explorers currently have telco data (including behaviour) from Orange and Fintonic data containing banking transactions (credit card, debit card, bank transfers, direct debits, paypal, etc.) in different sectors.

Fintonic's data pipelines are in Databricks and orchestrated through Databricks jobs. Then the data is sent to mlops s3, which triggers the import into Domo DB, where those datasets are linked to the cards within the dashboards, which are iframed into the Insights Store.

For Orange, this process is the same, except some steps for anonymisation sit on Orange's environment. We are not entirely sure what these are and have a spike to discover this and document it fully.

The current setup has served us well for some months and has allowed us to sell some Market Reports. It does present us with some challenges, though.

# **Challenges**

- **Brand/Product consistency.** We have two different analytics visualisation tools (Insights Explorer and Domo), which doesn’t give a consistent and good user experience. We also can’t make the most of the opportunities and solutions in one and the other (e.g. value brands problem is similar to the multiple market explorers problem).
- **We can't do** **Top Winners effectively**. We have this on two cards in a separate dashboard away from the rest of the insights. We have to curate an exploded dataset in order even to show this. Ideally, we want top winners everywhere where it would make sense.
- **Timeouts/lack of oversight**. Domo is sometimes very slow to query because of the large datasets. We don't have the oversight/control of how the data is being queried, where it's stored, etc, to improve this. It's just part of their product.
- **Having something done in Domo takes a long time;** therefore, any improvements are delayed.
- **Elevated cost** has been considered, and while not a reason to drive the change, it might be a positive side-effect of this initiative.
- **In house resources/skills/knowledge** to maintain and modify domo are reduced. Reduced in House knowledge on Domo.
- **We feel that the aesthetics, user experience and** **filter-flexibility** **of Domo is weaker than that of Insights Explorer.** (Truth is, that had IE been capable of delivering time series insights at the time, we would never have looked at Domo - or any other alternative - in the first place)

# **Justification**

Therefore, it is of strategic importance that we use the Insights Explorer platform to show the Market Explorers because:

- We know we can do top winners. We are currently doing it.
- We've proven we can serve quick insights for user-centric data.
- We'll not depend on a third-party company to develop a critical product.
- If the final solution is to display this data in the Insights Explorer, we'll:
  - Consolidate our analytics visualisation into a single tool.
  - Add some important features (time-based visualisation and analysis of insights) that we may be able to use in other scenarios.

# **Solution**

## Navigation from the Insights Store

- The user will visit the Insights Store and navigate to the different market explorers
- There will be an option to open a market explorer if the user is subscribed to it
- If the user decides to open a market explorer, they will be directed to the Market Explorer (that is, an Insights Explorer instance showing data for that market)

### **De-scoped**

- The subscription of a user in both tools will be done manually, there won’t be communication between the Insights Store and the Insights Explorer
- No SSO shared between the two, so the user will need to login twice.
- The Insights Explorer will open in a new window, it won’t be “embedded” into the Insights Store

## Landing into the Market Explorer

Once the user has selected one Market Explorer from the Insights Store (as above specified), they will land into the Market Explorer (an IE instance):

- The user will be presented with X different options (equivalent to the tabs we currently have)
- The user will select one option and will be presented with a dashboard with several cards laid out
- There will be a new card to show brand trends (to be scoped in a separate section)

### **De-scoped**

- There won’t be any new cards except for the one mentioned. That is, we won’t have the map card, for example.x
- English only interface, Market Explorer won’t be available in Spanish.



## Using the Market Explorer

- User can use filters as usual with the new filter interface. Can do so by searching or clicking on cards
- User can move cards around, but can’t add/remove any. This is because we want to control for now what is shown and we want to avoid yet-to-be-solved-problems around showing user-centric vs transation-centric data.
- If the user modifies this dashboard (e.g. moves a card), changes will be persisted

### **De-scoped**

- User can’t add/remove cards.  If removing this IE feature becomes a problem, we can leave it.
- No left menu
- We can consider de-scoping the filter search and allowing only clicking on cards to add a filter.

# Brand trends card

The use cases we collected and that we will support are the following:

- I'm just browsing the sector or competitors, not comparing, getting to trust the data
- I'm comparing one (my) brand with one or more competitors
- I'm comparing one (my) brand with the sector (that's everybody)

Characteristics of the card and how it interacts with the filters and other cards:

- Card will be able to show multiple lines depending on the user selection:
  - Card will always show a line for the sector
  - Card will show a line for your own brand
  - Card will show a line for each of the other brands you want to compare your brand to
- Users will be able to understand which line is which brand or sector
- Your brand will be defined by the brand in your audience bar
- Competitors brands will be defined by the brands in your baseline bar
- Other cards will work as usual (i.e. the full filter will apply)
- In the demos, we’ll prepare the audience and baseline bars with the filters as expressed below
- There will be 3 brand trends card, one will show the number of transactions, the other one the avg spent and a last one with the total spent.
- The X axis will show the aggregate by month.



# **Risks**

- **Technical**: we must validate that we can serve queries against time-based data within a specific latency and budget.
- **UX**: we'll need to ensure the user understands the different types of data shown and how they work with the filtering criteria, as we are mixing two different ways of interpreting the data (user-centric vs transaction-centric).
- External users in Orange or BT will need to be on-boarded again and made aware of the differences and limitations.
- Will users care about a difference in the tool? (subscribers who will need to switch from Domo to our new version?)

# **Conditions of Satisfaction**

- We can generate market reports with the new tool. Features that should be available for that to happen:
  - Filter by any field, as we currently can do
  - See "user-centric" cards (brands, age...) with top winners functionality
  - See monthly brand trends based on:
    - number of transactions
    - total spent
    - avg spent
- We will decommission Domo by the end of April 2024
- Existing users know how to use the new tool

# **Workstreams**

We believe there will be at least five workstreams dedicated to meeting this need:

1. **TechOps** may need to provision new data stores or environments, deploy new services, etc.
2. **Market eXchange team** will need to make sure the data is populated with the right schema and loaded into the appropriate data stores. They will also need to configure the tools so that the data is displayed as required.
3. **Insights Store team** will need to provide a solution to query time based data so that it can display the required insights applying the necessary filtering criteria.
4. **Insights Explorer team** will need to provide support for new visualisations into the IE.
5. **Customer Success** will need to on-board existing users into the new tool.



Done reading? Click here. → Claudia Teres, Helen Soniega, Darren McConnell, Phil Douty, David Darby, Nidhi Sharma, Jaekyoung Lee, Mark Bunn, Jonathan Lakin, Albert Pastrana

Helen Soniega, Darren McConnell, Phil Douty, David Darby, Anthony Channon, Jaekyoung Lee, Mark Bunn I’m aligned with the problems & goals

Jonathan Lakin, Lewis Longman-Jones I’m not aligned

 I’m aligned with the problem but not the solution



# Feedback

Add feedback

| Done | What is it that you want to share? | Author | Vote | Notes |
| --- | --- | --- | --- | --- |
| true | A nice doc, thanks for sharing Albert. I’m actually really excited to see the time series capability in IE and get the Market Explorer experience transformed by using IE - I think it’s going to be much better for the user | Anthony Channon | Claudia Teres, Albert Pastrana, Mark Bunn |  |
| false | I’m bought into the problems but not the conceptual solution... I worry we are trying to replicate domo vs thinking about the best way to think of a market report... so I think we should take more time to think that through... | Jonathan Lakin | Lewis Longman-Jones |  |
| false | I also think that to get what we want from a market report in IE will require us to have a big appetite for it, as I can see what’s being proposed here is really just a first step, and it could end up being a much bigger scope of work. I think we need to understand what that might look like and weigh up our appetite for this, vs fixing some of the Domo issues we have | Jonathan Lakin | Lewis Longman-Jones |  |
| false |  | Jonathan Lakin |  |  |
| false |  | Javier Pedreira |  |  |