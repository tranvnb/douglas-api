# Douglas API

A non-official Douglas College API.

## Architecture/Scope (Summer 2020)

We will use Strapi, a headless CMS, as our project monolith (API gateway and API endpoint in the same server). Strapi will allow us to create admin users who can manage API data and API permissions. It also has the abilitly to run functions, which we'll use to scrape for data, that follow CRON configurations. Another reason we're using Strapi is that we can manually collect data if the college somehow tells us to not ethically scrape their website.

We don't know how the API will be used yet or what it will ultimately contain, so let's keep it simple:

```
                                                               ┌─────────────┐                  
                                                               │ ┌─────────┐ │                  
                                ┌─ monolith ─────────────┐     │ │ aws rds │ │                  
                                │ ┌────────────┐         │     │ └─────────┘ │                  
                                │ │ strapi api <─────────┼─────> ┌────────┐  │                  
                ┌───────┐       │ └────────────┘         │     │ │ aws s3 │  │                  
internet <─────>│ nginx <───────> ┌──────────────┐       │     │ └────────┘  │                  
                └───────┘       │ │ strapi admin |       │     └─────────────┘                  
                                │ └──────────────┘       │                                      
                                │ ┌──────────────────┐   │            ┌─────────────────┐              
                                │ │ strapi functions ├───┼──scrapes───> douglas website │              
                                │ └──────────────────┘   │            └─────────────────┘              
                                └────────────────────────┘                                      
```                                            

Our proposed endpoints: `/program`, `/program/course`, `/professor`, `/deadlines`, `/clubs`, `/college-services`

## General timeline (Summer 2020)

- [ ] Request for comments (RFC) - share some ideas by opening issues, and submit pull requests with the implementation details of your idea
- [ ] Development
- [ ] Release a working version of the API to select developers
- [ ] Create documentation

## Why you need to contribute

In short, we'll be able to help jumpstart a wave of innovation in the college. Students from Douglas College will be able to use our API to create apps that enrich the lives of their peers.

## How to contribute

**You could open an issue in this repo to start discussions or to brainstorm ideas**, with the goal of creating a pull request with the implementation.

### RFCs

1. Fork this repo into your local machine.
2. Copy the `template.md` into `rfcs/my-feature-name.md` and add your work there.
3. Submit your pull request.
4. Be prepared to revise your pull request because it will be reviewed by other contributors.
5. At some point, the core team members will decide what to do with the pull request.

### Development

All contributors, including the core team members, have to send pull requests. These will be reviewed and it can either get merged, sent back to you for revisions, or closed with an explanation.

## Notes 

This document is subject to changes.
