# Objective

Update the critical front-end dependencies in the Insights Explorer (IE) project to improve performance, maintainability, and ensure long-term compatibility with modern web standards.

# Problem

The Insights Explorer project has several key dependency issues that, if left unaddressed, will continue to hinder development and performance:

- **Charting Library Obsolescence**: The library we currently use to render charts has been abandoned for over three years. This poses security risks, limits functionality, and hinders our ability to provide users with up-to-date data visualization features.
- **Outdated Build Tools**: Our core build tools, Webpack and Jest, are outdated, leading to:
  - Slow build times, impacting developer productivity.
  - Increased complexity and maintenance burden in our build scripts.
  - Sub-optimal client-side performance, affecting the end-user experience.
- **React Version Lag**: We are currently on React 17, while React 19 is about to be released. This lag creates several issues:
  - Some libraries we rely on require React 18 or higher, limiting our ability to update or leverage improvements in those libraries.
  - The effort required to upgrade increases exponentially with each major version we fall behind, creating compounding technical debt.

By addressing these issues, we can provide a more performant, maintainable, and future-ready Insights Explorer, enhancing both the development process and the end-user experience.

# Value

Updating our front-end dependencies in Insights Explorer will provide the following benefits:

1. **Modern Development Standards and Security**: As with any major release, React 18 includes bug fixes and security patches, ensuring your app stays up to date with the latest practices and has fewer vulnerabilities.
2. **Improved Maintainability**: Updating dependencies simplifies the codebase, reduces technical debt, and makes future updates easier and less time-consuming.
3. **Future-Proofing**: Moving to React 18 (with a pathway to React 19) ensures compatibility with current standards.
4. **Enhanced Performance**: Modern build tools and libraries will decrease build times, streamline the development process, and improve client-side performance, creating a faster, more responsive user experience.
5. **Improved Visualization Capabilities**: By adopting a modern, actively maintained charting library, we can offer better data visualizations with enhanced interactivity, visual appeal, and reliability.

## Additional benefits

### Impact on Hiring and Employee Retention

Addressing these critical front-end updates will not only improve our product but also positively impact our team dynamics, making Intent HQ a more attractive and supportive workplace for both current and future talent:

1. **Attracting Top Talent**: Engineers are drawn to roles where they can work with modern, efficient tools and frameworks that allow them to focus on meaningful problem-solving rather than grappling with outdated technology. By proactively updating the front-end dependencies in Insights Explorer, Intent HQ positions itself as a forward-thinking, developer-friendly environment that invests in the latest technologies, which is a major draw for top candidates evaluating their career options.
2. **Retaining Existing Talent**: Engineers working with slow build times, outdated tools, and abandoned libraries often experience frustration, as these barriers can hinder productivity and make daily work feel unnecessarily challenging. By addressing these pain points, we create a smoother, more enjoyable development experience. This fosters a positive work culture where engineers feel their feedback is valued, improving job satisfaction and reducing turnover.
3. **Encouraging Skill Growth and Development**: Working with updated technologies like React 18 (and soon React 19), modern charting libraries, and current build tools aligns with the skills developers want to build and stay competitive in the market. Offering these growth opportunities not only enhances our team’s capabilities but also deepens their commitment to Intent HQ, as they see their careers and skills advancing alongside the company’s evolution.

By making these necessary updates, Intent HQ becomes a place where engineers can do their best work with the best tools, ultimately supporting both hiring and retention goals in a competitive talent landscape.

### React 18 related benefits

1. **Updated Library and Ecosystem Support**: Many popular libraries are updating to support React 18’s new concurrent and Suspense features. By upgrading, you ensure compatibility with these libraries and benefit from improvements that take advantage of React 18’s features.
2. **Streaming Server-Side Rendering (SSR) with Suspense**: React 18 enhances SSR by allowing components to load in chunks rather than waiting for the entire page to load. It also enables streaming HTML to the browser as content is ready, improving perceived performance and letting users see something on the page faster. This can be an enabler to embed IE cards in Teams or Slack.

## Success metrics

- Time to run tests in local: reduced by 30%
- Build time in CI: reduced by 20%
- Build scripts complexity: 40% less lines of code.
- Number of parked front-end related dependency upgrades: reduced by 70%
- No usage of Plottable, Enzyme, Webpack and Jest
- React upgraded to version 18

# Appetite

6 weeks

# Solution

Our proposed solution involves a phased update approach.

1. **Library Updates**
   1. **Plottable:** replace the abandoned chart library with a well-supported alternative (`Nivo`, already chosen and used in IE), balancing compatibility with enhanced visualization capabilities.
   2. **Enzyme**: migrate remaining enzyme tests to `testing-library` (used by the majority of existing tests).
   3. **React 18**: incrementally upgrade any other critical libraries and dependencies to support React 18, ensuring stability and comprehensive testing with each update.
2. **Build Tool Overhaul**

Replace Webpack and Jest with Vite for faster builds. This will simplify build scripts, improving maintainability and reducing complexity.

## Risks

1. **Compatibility Issues and Breakages**: Updating multiple dependencies could introduce unforeseen compatibility issues, leading to potential downtime, delays, and extensive troubleshooting.
2. **Risk of Rabbit Holes**: Interconnected dependencies may lead developers into unrelated issues that expand the project scope and consume resources. Clear priorities and boundaries are essential to avoid scope creep.
3. **Regression Bugs in Older Code**: Updating older code increases the chance of regression bugs that could disrupt functionality. Comprehensive testing and monitoring are needed to minimize these risks.