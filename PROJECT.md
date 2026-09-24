# GSB-002 - Marketing AI Workflow Architect

## Project Type

Gradensal Signature Build

## Status

In Development

## Started

2026-09-24

## Author

Lissette Gorrin Rodriguez

## Organization

Gradensal

## Local Project Location

`/Users/lissettegorrin/Desktop/_Gradensal/Signature_Builds/marketing-ai-workflow-architect`

## Target Career Context

This Signature Build is inspired by the capabilities emphasized in Intuit's
Senior Developer — Marketing AI Development Lead role.

The project does not claim to reproduce Intuit's internal systems or establish
qualification for the role. It is an independent portfolio prototype designed
to demonstrate relevant architectural, AI, workflow, engineering, and
technical-communication skills.

## Problem

Organizations often jump from identifying an inefficient workflow directly to
asking for an AI agent.

That skips an important architecture decision:

What level of automation and autonomy does the workflow actually require?

## Product Hypothesis

A lightweight decision-support system can help teams reason more explicitly
about whether a workflow is better suited to:

1. deterministic automation;
2. an LLM-assisted workflow;
3. an agentic workflow; or
4. human-first execution or redesign.

## Core Architecture Principle

The language model will not independently determine the architecture.

A deterministic rules layer will make the primary recommendation from explicit
workflow characteristics.

An AI explanation layer may then translate that recommendation into useful
stakeholder language.

## Success Criteria

The first prototype is successful when it can:

- accept structured workflow information;
- classify representative workflows consistently;
- explain why a classification occurred;
- identify risk and human-approval requirements;
- expose the decision system through an API;
- provide a usable browser interface;
- demonstrate at least three distinct marketing workflow scenarios;
- pass automated tests;
- document its architecture and limitations clearly.