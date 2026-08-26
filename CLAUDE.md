# CLAUDE.md

*The instruction system for this vault. Read this first, every session.*

## How this works

- **At session start:** read `MEMORY.md` silently. Be informed by it, don't announce it.
- **Before working on a project:** read that project's `_CONTEXT.md` first. Find it in the routing map below.
- **When I say "remember this":** write it to the right file immediately, then confirm which file.
- **If the routing map has no match:** ask me rather than reading the whole vault.

## Where things go

| If it...                    | Goes in...                  |
| :-------------------------- | :-------------------------- |
| Is a rule ("always do X")   | `CLAUDE.md` (this file)     |
| Is a project fact or status | `ProjectFolder/_CONTEXT.md` |
| Is true across everything   | `MEMORY.md`                 |

**Keep `MEMORY.md` short.** It loads every session. Detail belongs in `_CONTEXT.md`, not there.

## Routing map

*Read the project's `_CONTEXT.md` when I mention any of these.*

<!-- Setup adds one row per project directly below the header row. -->

| Project | Trigger words | Context file |
| :------ | :------------ | :----------- |

> Empty until setup fills it in — see `01 START HERE (give this to your AI).md`.
> Trigger words should be whatever you'd actually type in a rush: short names,
> client names, teammate names, product names, and shorthand you use often.

## Creating a new project

When I mention something that clearly needs its own folder, do all three, in order, without asking permission — then confirm:

1. Create `ProjectName/_CONTEXT.md` from `_TEMPLATE_CONTEXT.md`. Fill what you know; use `unknown — ask me` for gaps.
2. Add a row to the routing map above.
3. Add one line to `MEMORY.md` under Active projects.

## Updating

After any session where something meaningful changed — status, a decision, a new person, a finished task:

- Update that project's `_CONTEXT.md`.
- If it's a fact that spans projects (a new person, a new company), also add it to `MEMORY.md`.
- Don't put project detail in `MEMORY.md`. Only cross-project facts go there.

## Pruning rule

Every time you write to a file, also remove what's no longer true:

| What | When to remove |
| :--- | :------------- |
| Open items `- [ ]` | Once done — delete the line, don't leave it checked |
| "What I Don't Know Yet" entries | Once answered — delete it, move the answer to the right section |
| People | When no longer involved |
| Routing map row | When the project closes |
| `MEMORY.md` row | When the project closes |

The goal: every line in every one of these files is true and useful *right now*. History belongs in the project's own notes, not in the context files.

## Preferences

*Filled in during setup — how I want you to respond.*

<!-- Setup replaces this line with real preferences. -->

---
*Context Router — pattern by Lim Jia Yong · @JiaYongLim1008*
